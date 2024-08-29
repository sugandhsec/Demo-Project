from django import forms
from .models import User

# class User(forms.Form):
#     username=forms.CharField( max_length=70, required=True,widget=forms.TextInput(attrs={"class": "special","disabled":True}))
#     email=forms.EmailField()
#     password=forms.CharField(max_length=200)

class UserForm(forms.ModelForm):
     class Meta:
         model = User
         fields ="__all__"

