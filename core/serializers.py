from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'codigo',
            'titulo',
            'conteudo',
            'estado',
            'categorias'
        )