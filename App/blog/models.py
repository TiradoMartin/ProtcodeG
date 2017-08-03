from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Entrada(models.Model):
    titulo = models.CharField(max_length=100,primary_key=True)
    contenido = RichTextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    fechacreacion = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    mensaje = RichTextField()
    identrada = models.ForeignKey(Entrada)

    def __str__(self):
        return str("%s %s " % (self.identrada,self.mensaje[:60]))


class Brainstoming(models.Model):
    titulo = models.CharField(max_length=100,primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    descrition = models.CharField(max_length=500)

    def __str__(self):
        return  str("%s %s" %(self.titulo,self.descrition[:60]))


class Menssege(models.Model):
    fechacreacion = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    mensaje = RichTextField(max_length=1000)
    identrada = models.ForeignKey(Brainstoming)

    def __str__(self):
        return str("%s %s " % (self.identrada,self.mensaje[:60]))

