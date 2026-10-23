from django.forms import ModelForm, forms, TextInput, Textarea, CharField, IntegerField, FileInput, NumberInput
from . models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'min_desc', 'desc', 'price', 'image']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Product Name'}),
            'min_desc' : Textarea(attrs={'placeholder': 'little description'}),
            'desc' : Textarea(attrs={'placeholder': 'Description'}),
            'price' : NumberInput(attrs={'placeholder': 'Price'}),
            'image' : FileInput(attrs={'class': 'form-control'})


        }
