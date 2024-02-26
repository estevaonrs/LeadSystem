from django.db import models
from django.utils import timezone
from django.utils.formats import number_format

class FipeVehicleType(models.Model):
    vehicle_type = models.CharField(max_length=100)

    def get_vehicle_type_display(self):
        translations = {
            "cars": "Carro",
            "motorcycles": "Moto",
            "trucks": "Caminhão",

            # Adicione mais traduções conforme necessário
        }
        return translations.get(self.vehicle_type, self.vehicle_type)

    def __str__(self):
        return self.vehicle_type

class FipeBrand(models.Model):
    brand = models.CharField(max_length=100)
    vehicle_type = models.ForeignKey(FipeVehicleType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} ({self.vehicle_type.vehicle_type})"

class FipeModel(models.Model):
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(FipeBrand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.model} ({self.brand.brand})"

class FipeYear(models.Model):
    year = models.IntegerField()
    model = models.ForeignKey(FipeModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.year} ({self.model.model})"

class FipeFuel(models.Model):
    fuel = models.CharField(max_length=50)
    year = models.ForeignKey(FipeYear, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fuel} ({self.year.year})"

class FipeCodeFipe(models.Model):
    code_fipe = models.CharField(max_length=50)
    model = models.ForeignKey(FipeModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code_fipe} ({self.model.model})"

class FipePrice(models.Model):
    price = models.CharField(max_length=50)
    brand = models.ForeignKey(FipeBrand, on_delete=models.CASCADE)
    model = models.ForeignKey(FipeModel, on_delete=models.CASCADE)
    fuel = models.ForeignKey(FipeFuel, on_delete=models.CASCADE)
    year = models.ForeignKey(FipeYear, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.price} ({self.model.model})"


CITY_CHOICES = [
    ("Abaiara", "Abaiara"),
    ("Acarape", "Acarape"),
    ("Acaraú", "Acaraú"),
    ("Acopiara", "Acopiara"),
    ("Aiuaba", "Aiuaba"),
    ("Alcântaras", "Alcântaras"),
    ("Altaneira", "Altaneira"),
    ("Alto Santo", "Alto Santo"),
    ("Amontada", "Amontada"),
    ("Antonina do Norte", "Antonina do Norte"),
    ("Apuiarés", "Apuiarés"),
    ("Aquiraz", "Aquiraz"),
    ("Aracati", "Aracati"),
    ("Aracoiaba", "Aracoiaba"),
    ("Ararendá", "Ararendá"),
    ("Araripe", "Araripe"),
    ("Aratuba", "Aratuba"),
    ("Arneiroz", "Arneiroz"),
    ("Assaré", "Assaré"),
    ("Aurora", "Aurora"),
    ("Baixio", "Baixio"),
    ("Banabuiú", "Banabuiú"),
    ("Barbalha", "Barbalha"),
    ("Barreira", "Barreira"),
    ("Barro", "Barro"),
    ("Barroquinha", "Barroquinha"),
    ("Baturité", "Baturité"),
    ("Beberibe", "Beberibe"),
    ("Bela Cruz", "Bela Cruz"),
    ("Boa Viagem", "Boa Viagem"),
    ("Brejo Santo", "Brejo Santo"),
    ("Camocim", "Camocim"),
    ("Campos Sales", "Campos Sales"),
    ("Canindé", "Canindé"),
    ("Capistrano", "Capistrano"),
    ("Caridade", "Caridade"),
    ("Cariré", "Cariré"),
    ("Caririaçu", "Caririaçu"),
    ("Cariús", "Cariús"),
    ("Carnaubal", "Carnaubal"),
    ("Cascavel", "Cascavel"),
    ("Catarina", "Catarina"),
    ("Catunda", "Catunda"),
    ("Caucaia", "Caucaia"),
    ("Ceará", "Ceará"),
    ("Cedro", "Cedro"),
    ("Chaval", "Chaval"),
    ("Choró", "Choró"),
    ("Chorozinho", "Chorozinho"),
    ("Coreaú", "Coreaú"),
    ("Crateús", "Crateús"),
    ("Crato", "Crato"),
    ("Croatá", "Croatá"),
    ("Cruz", "Cruz"),
    ("Deputado Irapuan Pinheiro", "Deputado Irapuan Pinheiro"),
    ("Ereré", "Ereré"),
    ("Eusébio", "Eusébio"),
    ("Farias Brito", "Farias Brito"),
    ("Forquilha", "Forquilha"),
    ("Fortaleza", "Fortaleza"),
    ("Fortim", "Fortim"),
    ("Frecheirinha", "Frecheirinha"),
    ("General Sampaio", "General Sampaio"),
    ("Graça", "Graça"),
    ("Granja", "Granja"),
    ("Granjeiro", "Granjeiro"),
    ("Groaíras", "Groaíras"),
    ("Guaiúba", "Guaiúba"),
    ("Guaraciaba do Norte", "Guaraciaba do Norte"),
    ("Guaramiranga", "Guaramiranga"),
     ("Hidrolândia", "Hidrolândia"),
    ("Horizonte", "Horizonte"),
    ("Ibaretama", "Ibaretama"),
    ("Ibiapina", "Ibiapina"),
    ("Ibicuitinga", "Ibicuitinga"),
    ("Icapuí", "Icapuí"),
    ("Icó", "Icó"),
    ("Iguatu", "Iguatu"),
    ("Independência", "Independência"),
    ("Ipaporanga", "Ipaporanga"),
    ("Ipaumirim", "Ipaumirim"),
    ("Ipu", "Ipu"),
    ("Ipueiras", "Ipueiras"),
    ("Iracema", "Iracema"),
    ("Irauçuba", "Irauçuba"),
    ("Itaiçaba", "Itaiçaba"),
    ("Itaitinga", "Itaitinga"),
    ("Itapajé", "Itapajé"),
    ("Itapipoca", "Itapipoca"),
    ("Itapiúna", "Itapiúna"),
    ("Itarema", "Itarema"),
    ("Itatira", "Itatira"),
    ("Jaguaretama", "Jaguaretama"),
    ("Jaguaribara", "Jaguaribara"),
    ("Jaguaribe", "Jaguaribe"),
    ("Jaguaruana", "Jaguaruana"),
    ("Jardim", "Jardim"),
    ("Jati", "Jati"),
    ("Jijoca de Jericoacoara", "Jijoca de Jericoacoara"),
    ("Juazeiro do Norte", "Juazeiro do Norte"),
    ("Jucás", "Jucás"),
    ("Lavras da Mangabeira", "Lavras da Mangabeira"),
    ("Limoeiro do Norte", "Limoeiro do Norte"),
    ("Madalena", "Madalena"),
    ("Maracanaú", "Maracanaú"),
    ("Maranguape", "Maranguape"),
    ("Marco", "Marco"),
    ("Martinópole", "Martinópole"),
    ("Massapê", "Massapê"),
    ("Mauriti", "Mauriti"),
    ("Meruoca", "Meruoca"),
    ("Milagres", "Milagres"),
    ("Milhã", "Milhã"),
    ("Miraíma", "Miraíma"),
    ("Missão Velha", "Missão Velha"),
    ("Mombaça", "Mombaça"),
    ("Monsenhor Tabosa", "Monsenhor Tabosa"),
    ("Morada Nova", "Morada Nova"),
    ("Moraújo", "Moraújo"),
    ("Morrinhos", "Morrinhos"),
    ("Mucambo", "Mucambo"),
    ("Mulungu", "Mulungu"),
    ("Nova Olinda", "Nova Olinda"),
    ("Nova Russas", "Nova Russas"),
    ("Novo Oriente", "Novo Oriente"),
    ("Ocara", "Ocara"),
    ("Orós", "Orós"),
    ("Pacajus", "Pacajus"),
    ("Pacatuba", "Pacatuba"),
    ("Pacoti", "Pacoti"),
    ("Pacujá", "Pacujá"),
    ("Palhano", "Palhano"),
    ("Palmácia", "Palmácia"),
    ("Paracuru", "Paracuru"),
    ("Paraipaba", "Paraipaba"),
    ("Parambu", "Parambu"),
    ("Paramoti", "Paramoti"),
    ("Pedra Branca", "Pedra Branca"),
    ("Penaforte", "Penaforte"),
    ("Pentecoste", "Pentecoste"),
    ("Pereiro", "Pereiro"),
    ("Pindoretama", "Pindoretama"),
    ("Piquet Caneiro", "Piquet Caneiro"), # Ajustado para Piquet Carneiro
    ("Pires Ferreira", "Pires Ferreira"),
    ("Poranga", "Poranga"),
    ("Porteiras", "Porteiras"),
    ("Potengi", "Potengi"),
    ("Potiretama", "Potiretama"),
    ("Quiterianópolis", "Quiterianópolis"),
    ("Quixadá", "Quixadá"),
    ("Quixelô", "Quixelô"),
    ("Quixeramobim", "Quixeramobim"),
    ("Quixeré", "Quixeré"),
    ("Redenção", "Redenção"),
    ("Reriutaba", "Reriutaba"),
    ("Russas", "Russas"),
    ("Saboeiro", "Saboeiro"),
    ("Salitre", "Salitre"),
    ("Santa Quitéria", "Santa Quitéria"),
    ("Santana do Acaraú", "Santana do Acaraú"),
    ("Santana do Cariri", "Santana do Cariri"),
    ("São Benedito", "São Benedito"),
    ("São Gonçalo do Amarante", "São Gonçalo do Amarante"),
    ("São João do Jaguaribe", "São João do Jaguaribe"),
    ("São Luís do Curu", "São Luís do Curu"),
    ("Senador Pompeu", "Senador Pompeu"),
    ("Senador Sá", "Senador Sá"),
    ("Sobral", "Sobral"),
    ("Solonópole", "Solonópole"),
    ("Tabuleiro do Norte", "Tabuleiro do Norte"),
    ("Tamboril", "Tamboril"),
    ("Tarrafas", "Tarrafas"),
    ("Tauá", "Tauá"),
    ("Tejuçuoca", "Tejuçuoca"),
    ("Tianguá", "Tianguá"),
    ("Trairi", "Trairi"),
    ("Tururu", "Tururu"),
    ("Ubajara", "Ubajara"),
    ("Umari", "Umari"),
    ("Umirim", "Umirim"),
    ("Uruburetama", "Uruburetama"),
    ("Uruoca", "Uruoca"),
    ("Varjota", "Varjota"),
    ("Várzea Alegre", "Várzea Alegre"),
    ("Viçosa do Ceará", "Viçosa do Ceará"),
]

class Lead(models.Model):
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    mileage = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    vehicle_type = models.ForeignKey('FipeVehicleType', on_delete=models.CASCADE)
    brand = models.ForeignKey('FipeBrand', on_delete=models.CASCADE)
    model = models.ForeignKey('FipeModel', on_delete=models.CASCADE)
    year = models.ForeignKey('FipeYear', on_delete=models.CASCADE) 
    fuel = models.ForeignKey('FipeFuel', on_delete=models.CASCADE) 
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    market_category = models.CharField(max_length=50, null=True, blank=True)
    car_category = models.CharField(max_length=50, null=True, blank=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pricing_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)  # Adicione este campo

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone}"

    def formatted_price(self):
        return "R$ " + number_format(self.price, 2, force_grouping=True, use_l10n=True)

    def formatted_original_price(self):
        return "R$ " + number_format(self.original_price, 2, force_grouping=True, use_l10n=True)

    def pricing_percentage_display(self):
        return f"{self.pricing_percentage * 100}%"
