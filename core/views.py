from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def obter_post_por_titulo(self, request, titulo=None):
        if titulo:
            try:
                post = Post.objects.get(titulo=titulo)
                serializer = self.get_serializer(post)
                return Response(serializer.data)
            except Post.DoesNotExist:
                return Response({'mensagem': 'Post não encontrado.'}, status=404)

        return Response({'mensagem': 'Parâmetro "titulo" não fornecido.'}, status=400)
    