from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def movie(request):
    return HttpResponse('<h1> POWER STAR<h1>')
def cinema(request):
    d={'name':'kushi'}
    return render(request,'cinema.html',context=d)