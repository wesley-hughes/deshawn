from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from deshawnapi.views import WalkerView, CityView, DogView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'walkers', WalkerView, 'walk')
router.register(r'cities', CityView, 'city')
router.register(r'dogs', DogView, 'dog')

urlpatterns = [
    path('', include(router.urls)),
]

