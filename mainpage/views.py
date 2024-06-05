from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def mainpagereturn(request):
    return render(request, 'index.html')

def optimizerreturn(request):
    return render(request, 'generic.html')

# Create your views here.