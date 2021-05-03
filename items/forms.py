from django import forms
from django.forms import widgets
from items.models import Item
from categories.models import Category

class ItemForm(forms.ModelForm):
    # categories = forms.ModelMultipleChoiceField(
    #     queryset=Category.objects.all(),
    #     widget=forms.CheckboxSelectMultiple(attrs={
    #         "id": "categories"
    #     })
    # )
    class Meta:
        model = Item
        fields = "__all__"


        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "id": "name"
            }),
            "categories": forms.SelectMultiple(attrs={
                "class": "form-control",
                "id": "categories"
            })

        }
