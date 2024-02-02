# forms.py
from django import forms
from .models import Lead, FipeBrand, FipeModel, FipeYear, FipeFuel, FipeVehicleType

class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = ['city', 'mileage', 'name', 'email', 'phone', 'vehicle_type', 'brand', 'model', 'year', 'fuel']

    def __init__(self, *args, **kwargs):
        super(LeadForm, self).__init__(*args, **kwargs)

        # Inicializa todos os campos relacionados como vazios
        self.fields['brand'].queryset = FipeBrand.objects.none()
        self.fields['model'].queryset = FipeModel.objects.none()
        self.fields['year'].queryset = FipeYear.objects.none()
        self.fields['fuel'].queryset = FipeFuel.objects.none()

        # Carrega os tipos de veículo
        self.fields['vehicle_type'].queryset = FipeVehicleType.objects.all()

        if 'vehicle_type' in self.data:
            try:
                vehicle_type_id = int(self.data.get('vehicle_type'))
                self.fields['brand'].queryset = FipeBrand.objects.filter(vehicle_type_id=vehicle_type_id).order_by('brand')
            except (ValueError, TypeError):
                pass  # Usuário forneceu uma entrada inválida; ignorar e deixar vazio

        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['model'].queryset = FipeModel.objects.filter(brand_id=brand_id).order_by('model')
            except (ValueError, TypeError):
                pass  # Usuário forneceu uma entrada inválida; ignorar e deixar vazio

        if 'model' in self.data:
            try:
                model_id = int(self.data.get('model'))
                self.fields['year'].queryset = FipeYear.objects.filter(model_id=model_id).order_by('year')
            except (ValueError, TypeError):
                pass  # Usuário forneceu uma entrada inválida; ignorar e deixar vazio

        if 'year' in self.data:
            try:
                year_id = int(self.data.get('year'))
                self.fields['fuel'].queryset = FipeFuel.objects.filter(year_id=year_id).order_by('fuel')
            except (ValueError, TypeError):
                pass  # Usuário forneceu uma entrada inválida; ignorar e deixar vazio

        # Se estiver editando uma instância existente, pré-carrega os campos relacionados
        if self.instance.pk:
            self.fields['brand'].queryset = self.instance.vehicle_type.fipebrand_set.order_by('brand')
            self.fields['model'].queryset = self.instance.brand.fipemodel_set.order_by('model')
            self.fields['year'].queryset = self.instance.model.fipeyear_set.order_by('year')
            self.fields['fuel'].queryset = self.instance.year.fipefuel_set.order_by('fuel')

    def save(self, commit=True):
        instance = super(LeadForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance
    
