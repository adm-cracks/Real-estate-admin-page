from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tenant(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pic/',default='./pic/contact.png')
    docu_prof = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pic/')
    location = models.CharField(max_length=220)
    features = models.TextField()
    area = models.FloatField(blank=True,null=True)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class units(models.Model):
    pro = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='pr')
    unit_type = models.CharField(max_length=10, choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')])
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.unit_type} -- {self.pro.name}"


class Rent(models.Model):
    tenant = models.ForeignKey(Tenant,related_name='tena',on_delete=models.CASCADE,blank=True,null=True)
    property = models.ForeignKey(Property,related_name='prop',on_delete=models.CASCADE)
    unit = models.ForeignKey(units,on_delete=models.CASCADE,blank=True,null=True)
    rent_date = models.IntegerField(blank=True,null=True)
    aggr_date = models.DateField()

    def __str__(self):
        return self.tenant.name