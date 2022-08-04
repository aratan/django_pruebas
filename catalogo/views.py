from django.shortcuts import render

# Create your views here.
from . models import Libro

#libros = Libro.objects.all().count()

def index(request):
    libro = Libro.objects.all().count()
    return render(
        request, 
        'index.html', 
        context={
            'libro': {libro},
            'titulo': 'Bienvenido a mi sitio'
            }
        )