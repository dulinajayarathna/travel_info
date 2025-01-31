from django.http import JsonResponse


def travel_tip(request):
    dest = request.GET.get("des", None)
    if dest:
        response = {"tip": f"Here are the details about {dest}"}
    else:
        response = {"tip": "always take your passport"}
    return JsonResponse(response)


def travel_tip_for_destination(request, destination):
    response = {"tip": f"Here are the details about {destination}"}
    return JsonResponse(response)
