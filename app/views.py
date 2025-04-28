from django.shortcuts import render

# Create your views here.
def jinga(request):
    d={'name':'RAMCHARAN'}
    return render(request,'jinga.html',context=d)