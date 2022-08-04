from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=64, help_text="Escribe el genero literario")

    def __str__(self):
        return self.name

class Libro(models.Model):
    titulo = models.CharField(max_length=64, help_text="Escribe el titulo del libro")
    fecha_publicacion = models.DateField(help_text="Escribe la fecha")
    
    #autor = models.ForeignKey(autor, on_delete=models.SET_NULL, null=True)
    #resumen = models.TextField(resumen,max_length=100, help_text="Escribe un resumen")
    #autor esta en otra tabla, si se borra que se permita allibro un autor null y no sea en cascada "
    #genero = models.ManyToManyField(Genero, help_text="Selecciona el genero")

    def __str__(self):
        return self.titulo