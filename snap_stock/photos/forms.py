from django import forms
from .models import Photo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'image', 'price']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'image': 'Изображение',
            'price': 'Цена'
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Добавляем поле email

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')