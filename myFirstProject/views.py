from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

def saludo(request):

    nombre = "Oscar"
    time =  datetime.datetime.now()
    works = ["Django", "Http protocol", "Rest"]

    #saludo_template = open("C:/python/DjangoProjects/myFirstProject/myFirstProject/templates/mytemplate.html")

    #my_template = Template(saludo_template.read())

    #saludo_template.close()

    my_template = loader.get_template("mytemplate.html")

    #ctx = Context({"nombre": nombre,"hora": time, "tareas": works})

    document = my_template.render({"nombre": nombre,"hora": time, "tareas": works})

    return HttpResponse(document)

def hora(request):

    time =  datetime.datetime.now()
    documento = f"""<html><body>

    <h1>La hora en bogota es : {time}

    </body></html>"""

    return HttpResponse(documento)