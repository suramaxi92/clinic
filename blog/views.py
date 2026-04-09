from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import patients

# Create your views here.
def index(request):
    page_title = "Index page"
    return render(request,"index.html", {"page_name": page_title})

def detail(request, id):
    Patients = patients.objects.get(id=id)
    return render(request, "details.html", {'patient': Patients})

def url_redirect(request):
    return redirect(reverse("blog:patients_list"))

def patients_list(request):
    page_title = "Patients List"
    #patients = [
    #   {"id": 1, "name": "John Doe", "age": 30},
    #   {"id": 2, "name": "Jane Smith", "age": 25},
    #   {"id": 3, "name": "Alice Johnson", "age": 40},
    #] 
    Patients = patients.objects.all()
    return render(request, "patients_list.html", {"page_name": page_title, "patients": Patients})

def add_patients(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        prescription = request.POST.get("prescription")
        new_patient = patients(name=name, age=age, prescription=prescription)
        new_patient.save()
        return redirect(reverse("blog:index"))
    return render(request, "add_patients.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        return render(request, "contact.html", {"success": True})
    return render(request, "contact.html")