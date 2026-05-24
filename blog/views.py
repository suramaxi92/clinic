from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from requests import request
from .models import patients, medicine

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
    medicines = medicine.objects.all()
    med_ids = request.POST.getlist("medicine")
    qtys = request.POST.getlist("quantity")
    prescription_text = ""
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        
        for i in range(len(med_ids)):
            med = medicine.objects.get(id=med_ids[i])
            qty = int(qtys[i])
            prescription_text += f"{med.name} - {qty}\n"
            med.quantity -= qty
            med.save()

        new_patient = patients(name=name, age=age, prescription=prescription_text)
        new_patient.save()
        return redirect(reverse("blog:index"))
    return render(request, "add_patients.html", {"medicines": medicines})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        return render(request, "contact.html", {"success": True})
    return render(request, "contact.html")

def add_medicine(request):
    success = False
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        new_medicine = medicine(name=name, quantity=quantity, price=price)
        new_medicine.save()
        success = True
    return render(request, "add_medicine.html", {"success": success})

def list_medicines(request):
    success = False
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        new_medicine = medicine(name=name, quantity=quantity, price=price)
        new_medicine.save()
        success = True
    medicines = medicine.objects.all()
    return render(request, "medicine_list.html", {"medicines": medicines})
