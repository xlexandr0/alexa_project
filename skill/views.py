from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Producto

@csrf_exempt
def alexa_endpoint(request):
    if request.method == "POST":
        data = json.loads(request.body)
        intent = data['request']['intent']['name']

        if intent == "AgregarProductoIntent":
            producto = data['request']['intent']['slots']['producto']['value']
            agregar_producto(producto)
            return JsonResponse({"response": f"{producto} agregado"})

        elif intent == "EliminarProductoIntent":
            producto = data['request']['intent']['slots']['producto']['value']
            eliminar_producto(producto)
            return JsonResponse({"response": f"{producto} eliminado"})

    return JsonResponse({"response": "Intent no reconocido"})

def agregar_producto(producto_nombre):
    producto, created = Producto.objects.get_or_create(nombre=producto_nombre)
    if not created:
        producto.cantidad += 1
    producto.save()

def eliminar_producto(producto_nombre):
    try:
        producto = Producto.objects.get(nombre=producto_nombre)
        if producto.cantidad > 1:
            producto.cantidad -= 1
        else:
            producto.delete()
    except Producto.DoesNotExist:
        pass

