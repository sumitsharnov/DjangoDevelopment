from django.contrib import admin

# Register your models here.
from .models import Pet

from .models import Vaccine

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']


@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    ist_display = ['name']
