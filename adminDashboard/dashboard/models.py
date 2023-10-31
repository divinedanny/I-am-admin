from django.db import models
from traderUser.models import TraderUser
# Create your models here.

class UserSales(models.Model):
    user = models.ForeignKey(TraderUser, on_delete=models.CASCADE)
    initial_deposit = models.IntegerField()
    profit = models.IntegerField()
    loss = models.IntegerField()
    net_equity = models.IntegerField()
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now=True)
    
# class Admin(models.Model):
#     user = models.ForeignKey(TraderUser, on_delete=models.CASCADE)
    
