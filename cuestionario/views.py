from django.shortcuts import render
from django.views.generic import DetailView, CreateView,UpdateView,DeleteView
from .models import Cuestionario, Pregunta, Opcion


# Create your views here.
class CrearView(CreateView):
    model = Pregunta
   
    fields = ['pregunta','cuestionario_id']
    template_name = 'crear.html'
    success_url = 'cuestionario/responder'

class ResponderView(DetailView):
    template_name = 'responder.html'

class ActualizarView(UpdateView):
    template_name = 'actualizar.html'

class EliminarView(DeleteView):
    template_name = 'eliminar.html'
