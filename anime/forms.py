from django import forms

from .models import *


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = {"name", "email", "text"}
