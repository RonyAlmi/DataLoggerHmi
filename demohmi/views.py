from django.shortcuts import render
from django.http import HttpResponse
from .models import valores

from .consumers import HmiConsumer

import threading
import time 

# Create your views here.
def inicio(request):
    #return HttpResponse("Listado de valores")
    valores_hmi=valores.objects.all()
    #print(valores_recv)
    return render(request, 'datos_hmi.html',{'valores_hmi':valores_hmi})

def graficos(request):
    return render(request, 'graficos.html')
