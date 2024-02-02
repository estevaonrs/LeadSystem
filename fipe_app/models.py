from django.db import models

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


class FipeData(models.Model):
    vehicle_type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    fuel = models.CharField(max_length=50)
    codeFipe = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.vehicle_type} - {self.brand} - {self.model} - {self.year} - {self.fuel} - {self.codeFipe} - {self.price}"


class Lead(models.Model):
    city = models.CharField(max_length=100)
    mileage = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    vehicle_type = models.ForeignKey('FipeVehicleType', on_delete=models.CASCADE)
    brand = models.ForeignKey('FipeBrand', on_delete=models.CASCADE)
    model = models.ForeignKey('FipeModel', on_delete=models.CASCADE)
    year = models.ForeignKey('FipeYear', on_delete=models.CASCADE) 
    fuel = models.ForeignKey('FipeFuel', on_delete=models.CASCADE) 
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Exemplo com DecimalField


    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone}"

