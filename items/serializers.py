from rest_framework import serializers
from items.models import Item
from categories.serializers import CategorySerializer
from categories.models import Category


class ItemSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Item
        fields = "__all__"

    def create(self, validated_data):
        cat_data = validated_data.pop("categories")
        item = Item.objects.create(**validated_data)
        categories = []
        for cat in cat_data:
            #Comment: Exploring customizing validation field to exclude name or create read only field
            cat_id = cat["id"]
            category = Category.objects.get(pk=cat_id)
            categories.append(category)
        item.categories.add(*categories)
        return item

    def update(self, instance, validated_data):
        cat_data = validated_data.pop("categories")
        instance.name = validated_data.get("name", instance.name)
        categories = []
        for cat in cat_data:
            cat_id = cat["id"]
            category = Category.objects.get(pk=cat_id)
            categories.append(category)
        instance.categories.set(categories)
        instance.save()
        return instance