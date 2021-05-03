from rest_framework import serializers
from categories.models import Category

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Category()._meta.get_field('id'))

    class Meta:
        model = Category
        fields = "__all__"

    
