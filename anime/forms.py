from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Reviews


class ReviewForm(forms.ModelForm):

    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = {"name", "email", "text", "captcha"}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border'}),
            'text': forms.Textarea(attrs={'class': 'form-control border'})
        }
