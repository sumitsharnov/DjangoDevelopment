from django.db import models

# Create your models here.
class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank = True)
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, blank = True, max_length=1)
    submission_date = models.DateTimeField()
    #age = models.Integer(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)
