from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Manufacturer(models.Model):
	mark = models.CharField(max_length=30)
	about_man = models.CharField(max_length=250)

	def get_absolute_url(self):
		return reverse('carrental:cars',
					   args=[self.mark])
	
	def __str__(self):		#funkcja konwertujaca do stringa, self to parametr przechowujacy aktualna instancje
		return self.mark	#zwracamy parametr mark(marke) w akutalnie przechowywanej instancji

	
class Engine(models.Model):
	engine_type = models.CharField(max_length = 40)
	capacity = models.IntegerField()
	combustion = models.FloatField()
	power = models.IntegerField()

	def __str__(self):
		return self.engine_type + ', ' + str(self.capacity) + ', ' + str(self.power)
		
		
class Car(models.Model):
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
	engine = models.ForeignKey(Engine, on_delete=models.CASCADE)
	model= models.CharField(max_length=30)
	course = models.IntegerField()
	year_of_production = models.DateField()
	color = models.CharField(max_length=30, default='brak')
	reg_number = models.CharField(max_length=7, default='brakrej')
	quantity = models.IntegerField(default=0)
	price = models.IntegerField()
	
	def get_absolute_url(self):
		return reverse('carrental:detail',
					   args=[self.model,
							 self.pk])					 
	
	def __str__(self):
		return self.model + '_' + str(self.pk)


class Comment(models.Model):
	car = models.ForeignKey(Car, related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)
	
	class Meta:
		ordering = ('created',)	
		
	def __str__(self):
		return 'Komentarz dodany przez {} dla samochodu {}'.format(self.name, self.car)


class PositionInOrder(models.Model):
	user = models.ForeignKey(User, unique=False)
	car = models.ForeignKey(Car) 
	quantityrc = models.IntegerField()  
	sincew = models.DateField()
	untilw = models.DateField()
	piosum = models.IntegerField()		#suma
	

	def __str__(self):
		return str(self.id)


class Order(models.Model):
	user = models.ForeignKey(User, unique=False)
	nr_doc = models.CharField(max_length=20)
	osum = models.IntegerField()
	pio = models.ManyToManyField(PositionInOrder)




	