from django.urls import path
from items.views import *

app_name = "items"

urlpatterns = [
    path("", views_page, name="items_views"),
    path("api/", views_index, name="items_index"),
    path("<int:pk>", views_show, name="items_show")  
]