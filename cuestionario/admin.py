from cuestionario.models import Pregunta
from django.contrib import admin
from .models import Pregunta, Cuestionario, Opcion

# Register your models here.
admin.site.register(Pregunta)
admin.site.register(Cuestionario)
admin.site.register(Opcion)