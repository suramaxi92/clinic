from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("patients/<int:id>/", views.detail, name="patient"),
    path("redirect/", views.url_redirect, name="url_redirect"),
    path("patients/", views.patients_list, name="patients_list"),
    path("add_patient/", views.add_patients, name="add_patients"),
    path("contact/", views.contact, name="contact"),

]