from django.db import models

# Create your models here.

class patients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    prescription = models.TextField()
    last_visit = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class medicine(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
