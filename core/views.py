from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def obter_post_por_titulo(self, request, titulo=None):
        if titulo:
            try:
                post = Post.objects.get(titulo=titulo)
                serializer = self.get_serializer(post)
                return Response(serializer.data)
            except Post.DoesNotExist:
                return Response({'mensagem': 'Post não encontrado.'}, status=404)

        return Response({'mensagem': 'Parâmetro "titulo" não fornecido.'}, status=400)
    
    