from django.db import models
from django.contrib.auth.models import User




class Menu(models.Model):
    """
    This Model is for to register user if they are coming to canteen
    to eat.
    """
    Date=models.DateField(unique=True)
    Vistors_list=models.ManyToManyField(User,blank=True)

    #Item list
    item1=models.CharField(blank=True,max_length=124)
    item2=models.CharField(blank=True,max_length=124)
    item3=models.CharField(blank=True,max_length=124)
    item4=models.CharField(blank=True,max_length=124)
    item5=models.CharField(blank=True,max_length=124)


    def __str__(self):
        return str(self.Date)
    
'Date','item1','item2','item3','item4','item5'