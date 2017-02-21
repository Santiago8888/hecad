from __future__ import unicode_literals 
from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
# Create your models here.

class Car(models.Model):
    vehiculo = models.CharField(max_length=30)
    valorCompra = models.IntegerField(default=0)
    fechaCompra = models.DateTimeField(auto_now_add=True)
    kilometraje = models.IntegerField(default=0)
    electrico = models.IntegerField(default=0)
    mecanico = models.IntegerField(default=0)
    llantas = models.IntegerField(default=0)
    accesorios = models.IntegerField(default=0)
    detallado = models.IntegerField(default=0)
    extras = models.IntegerField(default=0)
    depreciacion = models.IntegerField(default=0)
    costoMantenimiento = models.IntegerField(default=0)
    subTotal = models.IntegerField(default=0)
    valorVenta = models.IntegerField(default=0)
    profit = models.IntegerField(default=0)

    def __str__(self):
	return self.vehiculo


#class Question(models.Model):
 #   owner = models.ForeignKey(User, related_name='question_user', verbose_name='Owner')
  #  question_text = models.CharField(max_length=200)
   # pub_date = models.DateTimeField('date published')
    #question_body = models.CharField(max_length=1000)
    #def __str__(self):
	#return self.question_text


#class Comment(models.Model):
 #   question = models.ForeignKey(Question, on_delete=models.CASCADE)
  #  comment_text = models.CharField(max_length=600)
   # votes = models.IntegerField(default=0)
    #def __str__(self):
     #   return self.comment_text


