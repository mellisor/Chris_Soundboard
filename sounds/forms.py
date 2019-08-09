from django import forms
from .models import Category, SoundByte

class CategoryForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = Category

class SoundByteForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = SoundByte