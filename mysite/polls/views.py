from django.shortcuts import render
from django.http import JsonResponse

from polls.api import TemperatureApi

def getMinT(request):
    return JsonResponse(TemperatureApi.minT(), safe=False)

def getMaxT(request):
    return JsonResponse(TemperatureApi.maxT(), safe=False)

def getAverageT(request):
    return JsonResponse(TemperatureApi.averageT(), safe=False)
