from django.shortcuts import render
from App1.models import Producto, Categoria
from App1.serializers import ProductoSerializer, CategoriaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def producto_list(request):
    if request.method=='GET':
        productos = Producto.objects.all().order_by('nombre')
        ser = ProductoSerializer(productos, many=True)
        return Response(ser.data)

    if request.method=='POST':
        ser = ProductoSerializer(data = request.data)
        if(ser.is_valid()):
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def producto_detail(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        ser = ProductoSerializer(producto)
        return Response(ser.data)

    if request.method=='PUT':
        ser = ProductoSerializer(producto, data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def categoria_list(request):
    if request.method=='GET':
        categorias = Categoria.objects.all().order_by('nombre')
        ser = CategoriaSerializer(categorias, many=True)
        return Response(ser.data)

    if request.method=='POST':
        ser = CategoriaSerializer(data = request.data)
        if(ser.is_valid()):
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def categoria_detail(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        ser = CategoriaSerializer(categoria)
        return Response(ser.data)

    if request.method=='PUT':
        ser = CategoriaSerializer(categoria, data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
