from django.shortcuts import render
from App_entrega3.models import Alumno, ArteMarcial, Pelicula
from App_entrega3.forms import AlumnoFormulario, ArtemarcialFormulario, PeliculaFormulario
 #Create your views here.
def formulario_alumno(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        edad = request.POST['edad']

        alumno = Alumno(nombre=nombre, apellido=apellido, edad=edad)
        alumno.save()

       

    return render(request, 'App_entrega3/formulario_alumno.html')


def formulario_artemarcial(request):
    if request.method == "POST":
        estilo = request.POST['Estilo']
        pais = request.POST['Pais']
        zona = request.POST['Zona']

        artemarcial = ArteMarcial(estilo=estilo, pais=pais, zona=zona)
        artemarcial.save()

       
    return render(request, 'formulario_artemarcial.html')


def formulario_pelicula(request):
        titulo = request.POST['titulo']
        director = request.POST['director']
        duracion = request.POST['duracion']

        pelicula = Pelicula(titulo=titulo, director=director, duracion=duracion)
        pelicula.save()

       

        return render(request, 'formulario_pelicula.html')


def buscar(request):
    if request.method == "POST":
        consulta = request.POST['consulta']

    if consulta == "alumno":
        personas = Alumno.objects.all()
        return render(request, 'busqueda.html', {'personas': personas})
    elif consulta == "artemarcial":
            artemarcial = ArteMarcial.objects.all()
            return render(request, 'busqueda.html', {'artemarcial': artemarcial})
    elif consulta == "pelicula":
        peliculas = Pelicula.objects.all()
    return render(request, 'busqueda.html', {'peliculas': peliculas})

    return render(request, 'busqueda.html')

def saludar_con_html(request):
    contexto = {}
    http_response = render(
        
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    
    return http_response
