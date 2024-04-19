from django.db import models
from rest_framework import serializers, viewsets

class Mascotas(models.Model):
    ESPECIE = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('hamster', 'Hamster'),
    ]

    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    especie = models.CharField(max_length=20, choices=ESPECIE)
    fecha_creado = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}-{self.edad}-{self.fecha_creado}"

# Serializador para el modelo Mascotas
class MascotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascotas
        fields = ['id', 'nombre', 'edad', 'especie', 'fecha_creado']

# Vista de conjunto para el modelo Mascotas
class MascotasViewset(viewsets.ModelViewSet):
    queryset = Mascotas.objects.all()
    serializer_class = MascotasSerializer

