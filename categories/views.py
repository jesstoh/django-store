from django.shortcuts import render
from django.http import JsonResponse
from categories.serializers import CategorySerializer
from categories.models import Category
from items.models import Item
from items.serializers import ItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


# Create your views here.
@api_view(["GET", "POST"])
def views_index(request):
    if request.method == "POST":
        category = CategorySerializer(data=request.data)
        if category.is_valid():
            category.save()
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def views_show(request, pk):    
    category = Category.objects.get(pk=pk)
    items = category.items.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


