# -*- coding: utf-8 -*-


# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse



def index(request):
	return render(request,'index.html')

def index2(request):
	return render(request,'index2.html')


