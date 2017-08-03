from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Developer(models.Model):
	Developer = models.CharField(max_length=100,primary_key=True)
	Specialty = models.CharField(max_length=100)
	Technology = models.CharField(max_length=200)
	Development_tool =models.CharField(max_length=300)
	Email = models.EmailField(max_length=200)
	Photo = models.ImageField(upload_to="media/image",null=True,blank=True)
	Descrition = RichTextField(null=True,blank=True)

	def __str__(self):
		return self.Developer



class Developmet_group(models.Model):
	Name_goup =models.CharField(max_length=100,primary_key=True)
	Analiyst = models.OneToOneField("Developer",related_name="Developmet1",help_text="En este campo seleccione el nombre del desarrollado que estará a cargo de el equipo de desarrollo")
	Dveloper1 = models.OneToOneField("Developer",related_name="Developmet2",null=False,blank=False,help_text="En este campo seleccione el nombre del desarrollado que ocupará esta posición en el equipo de desarrollo")
	Dveloper2 = models.OneToOneField("Developer",related_name="Developmet3",null=True,blank=True,help_text="En este campo seleccione el nombre del desarrollado que ocupará esta posición en el equipo de desarrollo")
	Dveloper3 = models.OneToOneField("Developer",related_name="Developmet4",null=True,blank=True,help_text="En este campo seleccione el nombre del desarrollado que ocupará esta posición en el equipo de desarrollo")
	Dveloper4 = models.OneToOneField("Developer",related_name="Developmet5",null=True,blank=True,help_text="En este campo seleccione el nombre del desarrollado que ocupará esta posición en el equipo de desarrollo")
	Dveloper5 = models.OneToOneField("Developer",related_name="Developmet6",null=True,blank=True,help_text="En este campo seleccione el nombre del desarrollado que ocupará esta posición en el equipo de desarrollo ")
	Dveloper6 = models.ManyToManyField("Developer",related_name="Developmet7",help_text="Si su grupo de desarrollo es muy grande puede  utilizar este campo para agregar una cantidad de ilimitada de miembros a su grupo de desarrollo  ")
	Descrition = RichTextField(null=True,blank=True)


	def __str__(self):
		return self.Name_goup


