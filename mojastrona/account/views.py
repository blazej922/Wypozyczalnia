# -*- coding: utf-8 -*-

from django.shortcuts import render, resolve_url, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME 
from .forms import LoginForm, EditFaultForm, FaultCommentForm, UserRegistrationForm
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from carrental.models import Car, Order, PositionInOrder
from django.contrib.auth.models import User, Group
from models import Fault, FaultComment, Service
import datetime
from django.utils import timezone


def logout_view(request):

    logout(request)
    return render(request, 'registration/logged_out.html')


def register(request):

	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			return render(request, 'registration/register_done.html', {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()

	return render(request, 'registration/register.html', {'user_form': user_form})

@login_required(login_url='account:login')
def dashboard(request):

	if request.user.is_staff:
		return HttpResponseRedirect('/admin/')
	groups = request.user.groups.all()[0]
	group = str(groups)

	if group == "customer":
		current_user = request.user.id
		documents = PositionInOrder.objects.filter(user=current_user)
		total = 0
		for document in documents:
			total += document.piosum
		return render(request, 'account/dashboard.html', {'documents':documents, 'total':total, 'group':group})
	
	elif group == "assistant":
		return render(request, 'account/dashboard.html', {'group':group})

	elif group == "serviceman":
		faults = Fault.objects.all()
		faults_dictio = {}
		for fault in faults:
			comments = FaultComment.objects.filter(fault=fault.id)
			faults_dictio[fault] = comments 	
		time = datetime.date.today()
		services = Service.objects.all()
		dictio = {}
		for s in services:
			days = int((s.overview_over_date - time).days)
			if days < 10 and days > 0:
				dictio[s] = days
		dictioisu = {}
		for s in services:
			days = int((s.insurance - time).days)
			if days < 10 and days > 0:
				dictioisu[s] = days
		return render(request, 'account/dashboard.html', {'faults':faults, 'group':group, 'dictio':dictio, 'dictioisu':dictioisu, 'faults_dictio':faults_dictio})


@login_required(login_url='account:login')
def editfault(request, pk):

	if request.method == 'POST':
		form = EditFaultForm(request.POST)
		if form.is_valid():
			form = form.cleaned_data
			status = form['status_usterki']
			fault = Fault.objects.get(pk=pk)
			fault.status = status
			fault.save()
			return redirect('/account/dashboard/')		
	else:
		form = EditFaultForm()
		return render(request, 'account/editfault.html', {'form':form})


@login_required(login_url='account:login')
def AddFaultComment(request, pk):	
	
	if request.method == 'POST':
		form = FaultCommentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account/dashboard/')		
	else:
		form = FaultCommentForm(initial={'fault':pk})	
	return render(request, 'account/AddCComment.html', {'form' : form})


@login_required(login_url='account:login')
def cart(request):

	if request.user.is_staff:
		return HttpResponseRedirect('/admin/')

	groups = request.user.groups.all()[0]
	group = str(groups)

	if group == "customer":
		current_user = request.user.id
		documents = PositionInOrder.objects.filter(user=current_user)
		total = 0
		for document in documents:
			total += document.piosum
		return render(request, 'account/cart.html', {'documents':documents, 'total':total, 'group':group})
	else:
		return HttpResponse('Zaloguj go się jako klient aby mieć dostęp to tej opcji!')
	