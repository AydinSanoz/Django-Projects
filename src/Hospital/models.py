from django.db import models

# Create your models here.


class Hospital(models.Model):
    Hospital_name = models.CharField(max_length=50)
    Doctor_name = models.CharField(max_length=50)
    Clinic = models.CharField(max_length=50)
