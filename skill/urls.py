from django.urls import path
from . import views

urlpatterns = [
    path('alexa-webhook/', views.alexa_webhook, name='alexa_webhook'),
]
