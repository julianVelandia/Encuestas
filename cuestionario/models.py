from django.db import models

# Create your models here.

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=100)


    def __str__(self):
        return self.pregunta 
        
class Cuestionario(models.Model):
    title = models.CharField(max_length=30)
    pregunta_id = models.ForeignKey(Pregunta, on_delete=models.CASCADE, blank=True, null=True,default=None)   











