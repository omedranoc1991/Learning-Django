from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Hola oscar")

def hora(request):

    time =  datetime.datetime.now()
    documento = f"""<html><body>

    <h1>La hora en bogota es : {time}

    </body></html>"""

    return HttpResponse(documento)