from django import forms
from .models import UserRegister, Caracteres, WantedCaracteres, Message
from django.contrib.auth.forms import UserCreationForm

class Register(UserCreationForm):
    
    class Meta:
        model = UserRegister
        fields =["username","email","genre","profil_photo","phone_number","address","profession","status", "birthdate","spiritual_belief"]

    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if 'birthdate' in self.fields:
                self.fields['birthdate'].widget.attrs['type'] = 'date'


class Login(forms.Form):
    username=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class Caraceters_auth(forms.ModelForm):
    class Meta:
        model = Caracteres
        exclude = ["user"]


class WantedCaraceters_auth(forms.ModelForm):
    class Meta:
        model = WantedCaracteres
        #exclude = ["user"]
        fields = ["nerveux","nice","generous","likes_outings","likes_outings","frugal","misspent","available",
                  "smoker","drinks_wine","chapel","regular_prayer","has_car","has_house","has_bank_account",
                  "riche","polygamous_relationships"]

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["message_content","message_title"]




