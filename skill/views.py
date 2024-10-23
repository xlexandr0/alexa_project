# alexa_app/views.py
from django.http import JsonResponse
from django.shortcuts import render
from .models import Item
import json

def mostrar_items(request):
    # Obtener todos los elementos de la base de datos
    items = Item.objects.all()
    # Renderizar los datos a la plantilla
    return render(request, 'mostrar_items.html', {'items': items})

def alexa_webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        intent_name = data['request']['intent']['name']
        
        if intent_name == 'CreateItemIntent':
            item = data['request']['intent']['slots']['item']['value']
            # Lógica para crear un nuevo objeto
            return JsonResponse({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": f"{item} fue creado exitosamente."
                    }
                }
            })

        elif intent_name == 'ReadItemIntent':
            item = data['request']['intent']['slots']['item']['value']
            # Lógica para obtener información de un objeto
            return JsonResponse({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": f"Detalles de {item}: ..."  # Aquí añade detalles del objeto.
                    }
                }
            })

        elif intent_name == 'UpdateItemIntent':
            item = data['request']['intent']['slots']['item']['value']
            new_value = data['request']['intent']['slots']['new_value']['value']
            # Lógica para actualizar el objeto
            return JsonResponse({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": f"{item} fue actualizado a {new_value}."
                    }
                }
            })

        elif intent_name == 'DeleteItemIntent':
            item = data['request']['intent']['slots']['item']['value']
            # Lógica para eliminar el objeto
            return JsonResponse({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": f"{item} fue eliminado exitosamente."
                    }
                }
            })

        else:
            return JsonResponse({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": "Intento no reconocido."
                    }
                }
            })
