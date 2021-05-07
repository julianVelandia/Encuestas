from django.urls import path
from . import views


urlpatterns = [
    path('crear', views.CrearView.as_view(), name='crearView'),
    path('responder', views.ResponderView.as_view(), name='responderView'),
    path('actualizar', views.ActualizarView.as_view(), name='actualizarView'),
    path('eliminar', views.EliminarView.as_view(), name='eliminarView'),
]
