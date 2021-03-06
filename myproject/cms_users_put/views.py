from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages


# Create your views here.
def todo(request):
    salida = ""
    lista = Pages.objects.all()
    salida += "<html>\n\t<head>\n\t\t<link rel='stylesheet'"
    salida += "href='css/name.css'>\n\t</head>\n\n\t"
    salida += "<body>\n\t\t"
    salida += "Las paginas que hay son:<ul>"
    for fila in lista:
        salida += "<li>" + fila.name + "--" + fila.page 
    salida += "</ul>\n\t</body>\n</html>"
    return HttpResponse(salida)
    

def handler(request, recurso):
    salida = ""
    
    if request.method == "PUT":
            page = "<html>\n\t<head>\n\t\t<link rel='stylesheet'"
            page += "media='screen' href='/css/name.css'/>\n\t</head>\n\n\t"
            page += "<body>\n\t\t" + request.body + "\n\t</body>\n</html>"
            fila = Pages(name=recurso, page=page)
            fila.save()
            
    try:
        fila = Pages.objects.get(name=recurso)
        salida += fila.page
        return HttpResponse(salida)
    except Pages.DoesNotExist:
        return HttpResponseNotFound('Pagina no encontrada: /%s.' % recurso)

def handler_css(request, recurso):
    salida = ""
    if request.method == "PUT":
        fila = Pages(name=recurso, page=request.body)
        fila.save()
        
    try:
        fila = Pages.objects.get(name=recurso)
        salida += fila.page
        return HttpResponse(salida, content_type= "text/css")
    except Pages.DoesNotExist:
        return HttpResponseNotFound('Pagina no encontrada: /%s.' % recurso)
 
        
def notfound(request, recurso):
    return HttpResponseNotFound("No tenemos " + recurso)
