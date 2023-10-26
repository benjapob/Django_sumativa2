from django.shortcuts import render
from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

class ProductoList(APIView):
    def get(self, request):
        productos = Producto.objects.all().order_by('nombre')
        ser = ProductoSerializer(productos, many=True)
        return Response(ser.data)

class ProductoDetail(APIView):
    def get_object(self, pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        producto = self.get_object(pk)
        ser = ProductoSerializer(producto)
        return Response(ser.data)

class CategoriaList(APIView):
    def get(self, request):
        categorias = Categoria.objects.all().order_by('nombre')
        ser = CategoriaSerializer(categorias, many=True)
        return Response(ser.data)

class CategoriaDetail(APIView):
    def get_object(self, pk):
        try:
            return Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        categoria = self.get_object(pk)
        ser = CategoriaSerializer(categoria)
        return Response(ser.data)