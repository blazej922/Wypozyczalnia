# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.template import loader
from django.views.generic import FormView
from forms import MessageForm
# Create your views here.

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
			cd = form.cleaned_data
			statement = 'Pomyślnie wysłano wiadomość.'
			form.save()
			return render(request, 'contact/success.html', {'statement': statement})
    else:
        form = MessageForm()
    return render(request, 'contact/contact.html', {'form': form})

