from django.db import models

# Create your models here.
class Info(models.Model):
    full_name = models.CharField(max_length=100,default=None)
    tel = models.CharField(max_length=13,default=None)
    products = models.TextField(default=None)
    summ = models.CharField(max_length=90,default=None)
    date = models.DateField(null=True,auto_now_add=True)
    lifetime = models.DateField(null=True)