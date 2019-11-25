from django.contrib import admin

# Register your models here.
from .models import Pet

from .models import Vaccine

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    pass
