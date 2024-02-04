from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'  # This ensures all fields are used, including the new ones

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['vehicle_type'] = instance.vehicle_type.get_vehicle_type_display()
        representation['brand'] = instance.brand.brand
        representation['model'] = instance.model.model
        representation['year'] = instance.year.year
        representation['fuel'] = instance.fuel.fuel
        representation['market_category'] = instance.market_category
        representation['car_category'] = instance.car_category
        representation['original_price'] = instance.original_price
        representation['pricing_percentage'] = instance.pricing_percentage

        return representation
