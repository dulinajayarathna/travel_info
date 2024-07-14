from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def travel_tip(request):
    response = {"tip": "always take your passport"}
    return JsonResponse(response)


def travel_tip_for_destination(request, destination):
    response = {"tip": f"Here are the details about {destination}"}
    return JsonResponse(response)
