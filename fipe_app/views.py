from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LeadForm
from django.http import JsonResponse
from .models import FipeBrand, FipeModel, FipePrice, Lead, FipeFuel, FipeYear, FipeVehicleType, Lead
from django.contrib.humanize.templatetags.humanize import intcomma

import re


def get_brands(request, vehicle_type_id):
    brands = FipeBrand.objects.filter(vehicle_type_id=vehicle_type_id).values('id', 'brand')
    return JsonResponse(list(brands), safe=False)


def get_models(request, brand_id, vehicle_type_id):
    models = FipeModel.objects.filter(
        brand_id=brand_id, 
        brand__vehicle_type_id=vehicle_type_id
    ).values('id', 'model')
    return JsonResponse(list(models), safe=False)


def get_years(request, model_id):
    years = FipeYear.objects.filter(model_id=model_id).order_by('year').values('id', 'year')
    return JsonResponse(list(years), safe=False)


def get_fuels(request, year_id):
    fuels = FipeFuel.objects.filter(year_id=year_id).order_by('fuel').values('id', 'fuel')
    return JsonResponse(list(fuels), safe=False)


def index_view(request):
    return render(request, 'leads/index.html')


def currency_to_float(value):
    if isinstance(value, (float, Decimal)):
        return float(value)
    number_string = re.sub(r'[R$.\s]', '', value).replace(',', '.')
    return float(number_string)


def str_to_decimal(price_str):
    price_str = price_str.replace('R$', '').strip()
    price_str = price_str.replace('.', '').replace(',', '.')
    return Decimal(price_str)


def show_price(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    
    # Formatação do preço para string de moeda
    formatted_price = "R$ {:,.2f}".format(lead.price).replace(',', 'x').replace('.', ',').replace('x', '.')

    context = {
        'lead': lead,
        'price': formatted_price,
        'model': lead.model  # Assumindo que 'model' é um objeto relacionado e tem um campo 'model' que é uma string
    }
    return render(request, 'leads/show_price.html', context)


def step_1(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        mileage = request.POST.get('mileage')
        request.session['lead_data'] = {'city': city, 'mileage': mileage}
        return redirect('fipe_app:step_2')
    return render(request, 'leads/step-one-form.html')


def step_2(request):
    if request.method == 'POST':
        # Recupera os dados da sessão armazenados na etapa 1
        lead_data = request.session.get('lead_data', {})

        # Atualiza os dados da sessão com as escolhas feitas nesta etapa
        lead_data.update({
            'vehicle_type': request.POST.get('vehicle_type'),
            'brand': request.POST.get('brand'),
            'model': request.POST.get('model'),
            'year': request.POST.get('year'),
            'fuel': request.POST.get('fuel')
        })
        
        # Salva os dados atualizados na sessão
        request.session['lead_data'] = lead_data

        # Redireciona para a próxima etapa
        return redirect('fipe_app:step_3')

    # Carrega os tipos de veículos para exibir no formulário
    vehicle_types = FipeVehicleType.objects.all()
    return render(request, 'leads/step-two-form.html', {'vehicle_types': vehicle_types})


def step_3(request):
    if request.method == 'POST':
        # Recuperando os dados das etapas anteriores da sessão
        lead_data = request.session.get('lead_data', {})

        # Adicionando os novos dados recebidos pelo formulário
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Assegurando que a quilometragem é convertida para inteiro
        mileage = int(lead_data.get('mileage', 0))  # Convertendo para int, default como 0 se não existir

        # Listas de categorias de mercado
        BOM_MERCADO = ['NSX 3.0', 'Modelo3']
        RUIM_MERCADO = ['Integra GS 1.8', 'Modelo5', 'Modelo6']
        MERCADO_QUEIMADO = ['Legend 3.2/3.5', 'Modelo9']

        # Criando o objeto Lead (ajuste conforme a sua implementação de modelos)
        lead = Lead(
            city=lead_data.get('city'),
            mileage=mileage,  # Usando a variável convertida para int
            name=name,
            email=email,
            phone=phone,
            vehicle_type_id=lead_data.get('vehicle_type'),
            brand_id=lead_data.get('brand'),
            model_id=lead_data.get('model'),
            year_id=lead_data.get('year'),
            fuel_id=lead_data.get('fuel')
        )

        # Buscando a instância de preço correspondente
        price_instances = FipePrice.objects.filter(
            brand_id=lead.brand_id,
            model_id=lead.model_id,
            fuel_id=lead.fuel_id,
            year_id=lead.year_id
        )

        if price_instances.exists():
            price_instance = price_instances.first()
            try:
                price_value = currency_to_float(price_instance.price)
                original_price = price_value  # Armazena o preço original para referência

                # Tratamento de strings para comparação
                model_name = lead.model.model.strip().lower()
                bom_mercado_normalized = [m.lower().strip() for m in BOM_MERCADO]
                ruim_mercado_normalized = [m.lower().strip() for m in RUIM_MERCADO]
                mercado_queimado_normalized = [m.lower().strip() for m in MERCADO_QUEIMADO]

                category = "N/A"  # Categoria de mercado inicial
                applied_percentage = "N/A"  # Percentual aplicado inicial

                # Determinando o ajuste de preço baseado em quilometragem e categoria de mercado
                if mileage <= 75000:
                    if model_name in bom_mercado_normalized:
                        price_value *= 0.82
                        category = "Bom Mercado"
                        applied_percentage = "82%"
                    elif model_name in ruim_mercado_normalized:
                        price_value *= 0.72
                        category = "Ruim Mercado"
                        applied_percentage = "72%"
                if model_name in mercado_queimado_normalized:
                    price_value *= 0.50
                    category = "Mercado Queimado"
                    applied_percentage = "50%"
                elif mileage > 75000 and category == "N/A":
                    price_value *= 0.62
                    category = "Acima de 75k km"
                    applied_percentage = "62%"

                # Imprime informações no console
                print(f"Modelo: {model_name}, Categoria: {category}, Percentual: {applied_percentage}, Preço Original: R$ {original_price}, Preço Ajustado: R$ {price_value}")

                # Ajustando o preço do lead
                lead.price = price_value
                lead.save()
                return redirect('fipe_app:show_price', lead_id=lead.id)
            except ValueError:
                # Tratamento de erro de formato de preço
                return render(request, 'leads/step-three-form.html', {'error': "Formato de preço inválido."})
        else:
            # Tratamento para quando não existir preço cadastrado
            return render(request, 'leads/step-three-form.html', {'error': "Preço não cadastrado para este veículo."})

    # Renderizar o formulário para entrada dos dados finais
    return render(request, 'leads/step-three-form.html')




