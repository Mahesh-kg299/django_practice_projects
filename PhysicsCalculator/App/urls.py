from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('mass_to_energy/', views.MassToEnergys.as_view()),
    path('wavelength_to_freq/', views.WavelengthToFrequency.as_view()),  
    path('SC_radius_to_mass/', views.SCRadiusToMass.as_view()),  
    path('lorenz_factor/', views.LorenzFactor.as_view()),
]