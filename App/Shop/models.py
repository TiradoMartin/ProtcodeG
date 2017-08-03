from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Shop_app(models.Model):
	Nombre = models.CharField(max_length=100)
	imagen1 = models.ImageField(upload_to="media/Image")
	imagen2 = models.ImageField(upload_to="media/Image")
	imagen3 = models.ImageField(upload_to="media/Image")
	imagen4= models.ImageField(upload_to="media/Image")
	descripcion = RichTextField()

	def __str__(self):
		return self.Nombre


class Shop_game(models.Model):
	Nombre = models.CharField(max_length=100)
	imagen1 = models.ImageField(upload_to="media/Image")
	imagen2 = models.ImageField(upload_to="media/Image")
	imagen3 = models.ImageField(upload_to="media/Image")
	imagen4 = models.ImageField(upload_to="media/Image")
	descripcion = RichTextField()

	def __str__(self):
		return self.Nombre
