from django.db import models

# Create your models here.

class patients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    prescription = models.TextField()
    patient_img = models.URLField(max_length=200, null=True)
    last_visit = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
