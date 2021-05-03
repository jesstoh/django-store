from django.shortcuts import render
from items.models import Item
from items.serializers import ItemSerializer
from categories.serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from items.forms import ItemForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@api_view(["GET", "POST"])
def views_index(request):
    if request.method == "POST":
        item = ItemSerializer(data=request.data)
        if item.is_valid():
            item.save()
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(["GET", "DELETE", "PUT"])
def views_show(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == "DELETE":
        item.delete()
        return Response({"message": "item deleted"})
    if request.method == "PUT":
        serializer = ItemSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
    serializer = ItemSerializer(item, many=False)
    return Response(serializer.data)

def views_page(request):
    form = ItemForm()
    return render(request, "items/index.html", {"form": form})