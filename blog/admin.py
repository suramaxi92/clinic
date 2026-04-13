from django.contrib import admin
from .models import patients

# Register your models here.
class patientsAdmin(admin.ModelAdmin):
    search_fields = ['name',
                      ]
    list_filter = ['last_visit',
                   ]

admin.site.register(patients, patientsAdmin)