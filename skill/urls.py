from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.mostrar_items, name='mostrar_items'),
    path('alexa-webhook/', views.alexa_webhook, name='alexa_webhook'),
]
