from django.db import models
from carrental.models import Car
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class Fault(models.Model):
	car = models.ForeignKey(Car)
	user = models.ForeignKey(User, unique=False)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	status_choice = (
        ('reported', 'Zgloszone'),
        ('in_progress', 'W trakcie'),
        ('done', 'Naprawione'),
    )
	status = models.TextField(choices = status_choice, max_length=12, default='reported', )

	def get_absolute_url(self):
		return reverse('account:EditFault',
					   args=[self.pk])

	def __str__(self):
		return str(self.id)


class FaultComment(models.Model):
	fault = models.ForeignKey(Fault)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('account:AddCFault',
					   args=[self.pk])


class Service(models.Model):
	car = models.ForeignKey(Car)
	overview_over_date = models.DateField()
	last_oil_change = models.IntegerField()
	insurance = models.DateField()