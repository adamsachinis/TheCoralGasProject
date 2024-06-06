from django.urls import path

from . import views

urlpatterns = [
    path("mesa", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact/<int:gasTankId>", views.dynamic, name="contact"),
    path("", views.index3, name="index"),
]