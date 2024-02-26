from django.contrib import admin
from .models import FipeVehicleType, FipeBrand, FipeModel, FipeYear, FipeFuel, FipeCodeFipe, FipePrice, Lead

class FipeVehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle_type')

class FipeBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'vehicle_type')

class FipeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand')

class FipeYearAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'model')

class FipeFuelAdmin(admin.ModelAdmin):
    list_display = ('id', 'fuel', 'year')

class FipeCodeFipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code_fipe', 'model')

class FipePriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'model', 'brand',  'fuel')


class LeadAdmin(admin.ModelAdmin):
    list_display = ('city', 'mileage', 'name', 'email', 'phone', 'vehicle_type', 'brand', 'model', 'year', 'fuel', 'formatted_price', 'market_category', 'car_category', 'formatted_original_price', 'formatted_pricing_percentage', 'created_at')

    def formatted_price(self, obj):
        return f"R$ {obj.price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    formatted_price.short_description = 'Price'

    def formatted_original_price(self, obj):
        return f"R$ {obj.original_price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    formatted_original_price.short_description = 'Original Price'

    def formatted_pricing_percentage(self, obj):
        return f"{obj.pricing_percentage * 100}%"
    formatted_pricing_percentage.short_description = 'Pricing Percentage'

admin.site.register(Lead, LeadAdmin)
admin.site.register(FipeVehicleType, FipeVehicleTypeAdmin)
admin.site.register(FipeBrand, FipeBrandAdmin)
admin.site.register(FipeModel, FipeModelAdmin)
admin.site.register(FipeYear, FipeYearAdmin)
admin.site.register(FipeFuel, FipeFuelAdmin)
admin.site.register(FipeCodeFipe, FipeCodeFipeAdmin)
admin.site.register(FipePrice, FipePriceAdmin)
