from django.urls import path
from categories.views import *

# app_name = "cat"

urlpatterns = [
    path("", views_index, name="cat_index"),
    path("<int:pk>", views_show, name="cats_show"),
]