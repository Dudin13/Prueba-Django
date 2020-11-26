from django.db import models

# Create your models here.

class Usuario(models.Model):
    username=models.CharField(max_length=250)
    email=models.EmailField()
    password=models.CharField(max_length=30)

class Idea(models.Model):
    private=((1,"publica"),(2,"protegida"),(3,"privada"))
    texto=models.CharField(max_length=250)
    visibility=models.CharField(max_length=1, choices=private)
    fecha=models.DateField()

class Solicitud(models.Model):
    respuesta=((0, "pendiente"),(1,"aceptado"),(2,"rechazado"))
    usernamerequest=models.ForeignKey(Usuario,on_delete=models.CASCADE,default=0)
    usernameinvate=models.CharField(max_length=250)
    status=models.CharField(max_length=1, choices=respuesta, default=0)
