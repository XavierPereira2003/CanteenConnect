from django.db import models
from django.contrib.auth.models import User



class Menu(models.Model):
    """
    This Model is for to register user if they are coming to canteen
    to eat.
    """
    Date=models.DateField(unique=True,primary_key=True)
    Course=models.JSONField(default=list,blank=True)
    Vistors_list=models.ManyToManyField(User,blank=True)

    def __str__(self):
        return str(self.Date)
    

    