from django.shortcuts import render
from django.views.generic import DetailView, CreateView,UpdateView,DeleteView



# Create your views here.
class CrearView(CreateView):
    template_name = 'crear.html'

class ResponderView(DetailView):
    template_name = 'responder.html'

class ActualizarView(UpdateView):
    template_name = 'actualizar.html'

class EliminarView(DeleteView):
    template_name = 'eliminar.html'
