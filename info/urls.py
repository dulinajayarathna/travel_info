from django.urls import path

from info import views

urlpatterns = [
    path("travel-tip/", views.travel_tip),
    path("travel-tip/<str:destination>/", views.travel_tip_for_destination)
]
