from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'home.html',{'name':'Akhanda'})
def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    r=val1+val2
    return render(request,'result.html',{'result':r})
def login(request):
    return render(request,'blabla.html')
def voting(request):
    return render(request,'onlinevoting.html')
