from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bunny(request):
    return HttpResponse('string from app1')
def laddu(request):
    return HttpResponse('fan of allu arjun')

