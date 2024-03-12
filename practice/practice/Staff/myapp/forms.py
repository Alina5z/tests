from .models import Task
from django.forms import ModelForm, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "place", "price", "square"]
        widgets ={
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара',
                'required': 'True',
            }),
            "place": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Объём',
                'required': 'True',
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',
                'required': 'True',
            }),
            "square": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество',
                'required': 'True',
            }),
        }