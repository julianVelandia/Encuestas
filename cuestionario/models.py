from django.db import models

# Create your models here.


class Cuestionario(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title 


class Pregunta(models.Model):
    pregunta = models.CharField(max_length=100)
    cuestionario_id = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)   

    def __str__(self):
        return self.pregunta 

class Opcion(models.Model):
    opcion = models.CharField(max_length=100)
    es_correcta = models.BooleanField()

    pregunta_id = models.ForeignKey(Pregunta, on_delete=models.CASCADE)   

        











