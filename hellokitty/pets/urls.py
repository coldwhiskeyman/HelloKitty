from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.get_pets, name='get_pets'),
    path('add', views.add_pet, name='add_pet'),
    path('pets/', views.PetList.as_view(), name='pet-list'),
    path('pets/<int:pk>/', views.PetDetail.as_view(), name='pet-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
