from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .physicalConstants import *
from math import sqrt

# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'App/Home.html')

class MassToEnergys(View):
    def get(self, request):
        return render(request, 'App/MassToEnergy.html')
    def post(self, request):
        mass = request.POST['mass']
        if mass:
            mass = float(mass)
        else:
            mass = 0
        energy = mass * c_2
        return JsonResponse({
            'value': '{:e}'.format(energy)
        })

class WavelengthToFrequency(View):
    def get(self, request):
        return render(request, 'App/WavelengthToFrequency.html')
    def post(self, request):
        wavelength = request.POST['wavelength']
        if wavelength:
            wavelength = float(wavelength)
        else:
            wavelength = 0
        frequency = c / wavelength
        return JsonResponse({
            'value': '{:e}'.format(frequency)
        })

class SCRadiusToMass(View):
    def get(self, request):
        return render(request, 'App/SCRadiusToMass.html')
    def post(self, request):
        radius = request.POST['radius']
        unit = int(request.POST['unit'])
        if radius:
            radius = float(radius)
        else:
            radius = 0
        mass = (c ** 2 / (2 * G)) * radius * unit
        return JsonResponse({
            'value': '{:e}'.format(mass)
        })

class LorenzFactor(View):
    def get(self, request):
        return render(request, 'App/LorenzFactor.html')
    def post(self, request):
        velocity = request.POST['velocity']
        if velocity:
            velocity = float(velocity)
        else:
            velocity = 0
        
        if velocity < 1:
            lf = 1 / sqrt(1 - velocity ** 2)
            return JsonResponse({
                'value': '{:e}'.format(lf)
            })
        return JsonResponse({
            'value': 'inf'
        })
