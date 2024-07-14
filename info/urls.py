from django.urls import path

from info import views

urlpatterns = [
    path("travel-tip/",views.travel_tip)
]
