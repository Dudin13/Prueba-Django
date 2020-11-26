from rest_framework import serializers
from .models import Usuario, Idea, Solicitud

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password']

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ['id', 'private', 'texto', 'visibility', 'frecha']

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['id', 'usernamerequest', 'usernameinvate', 'status']
