from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('investor', 'Investor'),
        ('guider', 'Guider'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="investor")

class Investor(models.Model):
    # id=models.CharField(max_length=8)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    # password=models.CharField(max_length=15)
    mobile_no=models.IntegerField(null=True,blank=True)
    investedAmount=models.IntegerField(null=True,blank=True)
    payementDate=models.DateField(null=True,blank=True)
    ispaid=models.BooleanField(default=False)

        


class Manager(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    # password=models.CharField(max_length=15)
    mobile_no=models.IntegerField()




class Guider(models.Model):
    # id=models.CharField(max_length=8)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    # password=models.CharField(max_length=15)
    # mobile_no=models.IntegerField(null=True,blank=True)
    experties=models.CharField(max_length=10)
    availibility=models.BooleanField(null=True,blank=True)
    isSelected=models.BooleanField(null=True,blank=True)



class Stock(models.Model):
    # symbol=models.CharField()
    name=models.CharField(max_length=40)
    current_price=models.FloatField()
    volume=models.IntegerField()
    sector=models.CharField(max_length=30)
    
class InvestorStock(models.Model):
    investor_id=models.CharField(max_length=8)
    stock_symbol=models.CharField(max_length=20)
    no_of_purchase=models.IntegerField()
    price_of_buy=models.FloatField()



class Watchlist(models.Model):
    investor_id=models.CharField(max_length=8)
    createdDate=models.DateField()


class Webinar(models.Model):
    guider_id=models.CharField(max_length=8)
    title=models.CharField(max_length=20)
    date_time=models.DateTimeField()
    duration=models.IntegerField()
    number_of_attendee=models.IntegerField()


# Create your models here.