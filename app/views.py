from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('MEGASTAR IS THE GOD OF INDAIAN CINEMA')
def jinga(request):
    d={'name':'RAMCHARAN'}
    return render(request,'jinga.html',context=d)