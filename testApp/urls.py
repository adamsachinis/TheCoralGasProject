from django.urls import path

from . import views

urlpatterns = [
    path("mesa", views.index, name="index"),
    path("", views.index2, name="index"),
]