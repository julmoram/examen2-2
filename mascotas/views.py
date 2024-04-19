from django.shortcuts import render

# Create your views here.
from .serializer import MascotasSerializer
from .models import Mascotas
from rest_framework import viewsets

class MascotasViewset(viewsets.ModelViewSet):
    queryset=Mascotas.objects.all()
    serializer_class=MascotasSerializer