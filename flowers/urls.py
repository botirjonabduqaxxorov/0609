from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flowers/', views.all_flowers, name='all_flowers'),
    path('flowers/type/<int:type_id>/', views.flowers_by_type, name='flowers_by_type'),
    path('flower/<int:pk>/', views.flower_detail, name='flower_detail'),
    path('types/', views.list_types, name='list_types'),
]
