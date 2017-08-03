from django.db import models
from App.Developmet_group.models import  Developmet_group
from ckeditor.fields import RichTextField
"""
Desarrollada por Martin Antonio Tirado M.
Version 1.0.0
Aplicacion de Aministración de proyecto de app 
Para la plataforma de ......
Creada entre 19/5/2017 y 

 Create your models here.
"""
class Aplication_log(models.Model):
	Name = models.CharField(max_length=100,null=False,primary_key=True)
	Estate_opc =(("1","En desarrollo"),("2","En producción"),("3","Indefinido"),("4","Concluido"))
	Estate = models.CharField(max_length=50,choices=Estate_opc)
	Group_developer = models.ForeignKey(Developmet_group,null=True,blank=True,on_delete=models.CASCADE)
	Store = models.ManyToManyField("Shop",related_name="Shopclient1")
	Estate_sopc =(("1","Publicada"),("2","En Proceso"),("3","En certificación"),("4","Eliminada",),("5","Indefinido"))
	State_Store = models.CharField(max_length=100,choices=Estate_sopc,null=True,blank=True)
	URL_store = models.URLField(max_length=300,null=True,blank=True)
	Console_Developer = models.URLField(max_length=300,null=True,blank=True)
	Client = models.ManyToManyField("Shop_client",related_name="Shop_client2")
	API = models.ForeignKey("API_Tools",related_name="Aplication_log4")
	Type_app =models.CharField(max_length=100)
	Means = models.ManyToManyField("Resouces_tools")       #recursos
	Device = models.CharField(max_length=100,null=True,blank=True)
	Monetization = models.CharField(max_length=100,null=True,blank=True)
	Photo1 = models.ImageField(upload_to="media/Image",null=True,blank=True)
	Photo2 = models.ImageField(upload_to="media/Image",null=True,blank=True)
	Photo3 = models.ImageField(upload_to="media/Image",null=True,blank=True)
	Photo4 = models.ImageField(upload_to="media/Image",null=True,blank=True)
	VCS = models.ForeignKey("VCS",related_name="Aplication_log5",null=True,blank=True)
	Key_project = models.CharField(max_length=100,null=True,blank=True)
	URL_VCS = models.URLField(max_length=300,null=True,blank=True)
	Packages = models.FileField(upload_to ="media/Packges",null=True,blank=True)
	Description = RichTextField()
	Date =models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.Name


class Shop_client(models.Model):
     Client = models.CharField(max_length=100,primary_key=True)
     URL_client = models.URLField(max_length=300,null=True,blank=True)
     Commentary = RichTextField(null=True,blank=True)
    

     def __str__(self):
     	return self.Client


class Shop(models.Model):
     Store = models.CharField(max_length=100,primary_key=True)
     URL_store = models.URLField(max_length=300,null=True,blank=True)
     Commentary = RichTextField(null=True,blank=True)

     def __str__(self):
     	return self.Store



class Resouces_tools(models.Model):
     Means = models.CharField(max_length=100,primary_key=True)
     Utility = models.CharField(max_length=100)
     URL_tools = models.URLField(max_length=300)
     User= models.CharField(max_length=100,null=True,blank=True)
     Password = models.CharField(max_length=100,null=True,blank=True)
     Email = models.EmailField(max_length=254,null=True,blank=True)
     Type_app = models.CharField(max_length=100)
     Commentary = RichTextField(null=True,blank=True)

     def __str__(self):
     	return self.Means


class VCS(models.Model):
	VCS = models.CharField(max_length=100,primary_key=True)
	URL_VCS = models.URLField(max_length=300)
	User= models.CharField(max_length=100)
	Password = models.CharField(max_length=100)
	Email = models.EmailField(max_length=254)

	def __str__(self):
		return self.VCS


class API_Tools(models.Model):
	Business = models.CharField(max_length=100,primary_key=True)
	Platform = models.CharField(max_length=100)
	API = models.CharField(max_length=100)
	URL_Platform = models.URLField(max_length=300)
	User= models.CharField(max_length=100)
	Password = models.CharField(max_length=100)
	Email = models.EmailField(max_length=254)
	Description = RichTextField()

	def __str__(self):
		return self.Business




class Developer(models.Model):
	Name = models.OneToOneField("Aplication_log",related_name="Aplication_log6",on_delete=models.CASCADE,primary_key=True)
	Estate_opc =(("1","En desarrollo"),("2","En producción"),("3","Indefinido"),("4","Concluido"))
	Estate = models.CharField(max_length=100,choices=Estate_opc)
	Group_developer = models.ForeignKey(Developmet_group,null=True,blank=True,on_delete=models.CASCADE)
	Client = models.ManyToManyField("Shop_client",related_name="Aplication_log7")
	Store = models.ManyToManyField("Shop",related_name="Aplication_log8")
	Device = models.CharField(max_length=100,null=True,blank=True)
	VCS = models.ForeignKey("VCS",related_name="Aplication_log10",null=True,blank=True)
	URL_VCS = models.URLField(max_length=300,null=True,blank=True)
	Packages = models.FileField(upload_to="media/Packages",null=True,blank=True)
	API= models.ManyToManyField("API_Tools",related_name="Aplication_log11")
	Type_app = models.CharField(max_length=100)
	Date_start= models.DateTimeField()
	Data_finish = models.DateTimeField()
	Records_note = RichTextField(null=True,blank=True)

	def __str__(self):
		return self.Name