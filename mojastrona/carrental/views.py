# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Manufacturer, Car, Comment
from account.models import Service
from .forms import CommentForm, PositionInOrderForm
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core import serializers
from django.contrib.auth.models import User, Group
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
import datetime

def index(request):
	
	marks = Manufacturer.objects.all()
	return render(request, 'carrental/index.html', {'marks' : marks})


def cars(request, mark):
	
	cars = Car.objects.filter(manufacturer__mark = mark)
	return render(request, 'carrental/cars.html', {'cars' : cars})


def detail(request, model, pk):
	
	car_detail = get_object_or_404(Car,
						     model = model,
							 pk = pk)						 
	comments = Comment.objects.filter(car_id=pk)						
	return render(request, 'carrental/detail.html', {'cardetail' : car_detail, 'comments' : comments})
	

@login_required(login_url='account:login')
def AddComment(request, model, pk):	
	
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.car_id = pk
			new_comment.save()
			statement = u"Pomyślnie dodano komentarz!"
			return render (request, 'carrental/Success.html', {'statement':statement})		
	else:
		form = CommentForm()		
	return render(request, 'carrental/AddComment.html', {'form' : form})


@login_required(login_url='account:login')
def AddToOrder(request, model, pk):

	car = get_object_or_404(Car,
                            model = model,
							pk = pk)
	current_user = request.user.id
	if request.method == 'POST':
		form = PositionInOrderForm(request.POST)
		if form.is_valid():
			newposition = form.save(commit=False)
			if newposition.quantityrc <= car.quantity:
				newposition.piosum = newposition.quantityrc * car.price * int((newposition.untilw - newposition.sincew).days)
				newposition.save()
				return redirect('/carrental/{model}/{id}/AddToOrder'.format(model=car.model, id=car.pk), {})
			else:
				return HttpResponse('Niestety nie mamy tyle samochodów na stanie')
	else:
		form = PositionInOrderForm(initial={'car':car, 'piosum':0, 'user':current_user})
	return render(request, 'carrental/orderposition.html', {'form' : form, 'car' : car})		


@login_required(login_url='account:login')
def insurenceedit(request, pk, model):

	if request.method == 'POST':
		car = get_object_or_404(Car,
                            model = model,
							pk = pk)
		service_document = Service.objects.get(car=car)
		new_date = request.POST["new_date"]
		service_document.insurance = new_date
		service_document.save()
		return redirect('/account/dashboard/')
	else:
		return render(request, 'carrental/insurence_edit.html', {})


@login_required(login_url='account:login')
def overviewedit(request, pk, model):

	if request.method == 'POST':
		car = get_object_or_404(Car,
                            model = model,
							pk = pk)
		service_document = Service.objects.get(car=car)
		new_date = request.POST["new_date"]
		service_document.overview_over_date = new_date
		service_document.save()
		return redirect('/account/dashboard/')
	else:
		return render(request, 'carrental/overview_edit.html', {})