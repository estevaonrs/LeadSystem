# urls.py

from django.urls import path
from .views import show_price, get_brands, get_models, get_years, get_fuels, index_view, step_1, step_2, step_3

app_name = 'fipe_app'

urlpatterns = [
    path('', index_view, name='index'),
    path('step_1/', step_1, name='step_1'),
    path('step_2/', step_2, name='step_2'),
    path('step_3/', step_3, name='step_3'),
    path('price/<int:lead_id>/', show_price, name='show_price'),
    path('get_brands/<int:vehicle_type_id>/', get_brands, name='get_brands'),
    path('get_models/<int:brand_id>/<int:vehicle_type_id>/', get_models, name='get_models'),
    path('get_years/<int:model_id>/', get_years, name='get_years'),
    path('get_fuels/<int:year_id>/', get_fuels, name='get_fuels'),
]
