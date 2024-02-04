from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['vehicle_type'] = instance.vehicle_type.get_vehicle_type_display()
        representation['brand'] = instance.brand.brand
        representation['model'] = instance.model.model
        representation['year'] = instance.year.year
        representation['fuel'] = instance.fuel.fuel
        # Since categoria_mercado and categoria_carro are string fields, just assign them directly
        representation['categoria_mercado'] = instance.categoria_mercado
        representation['categoria_carro'] = instance.categoria_carro

        return representation
