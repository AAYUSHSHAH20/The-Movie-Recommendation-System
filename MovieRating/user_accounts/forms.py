from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.models import User 

class UserCreateForm(UserCreationForm):

    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "age")

    def __init__(self, *args, **kwargs):        
        super(UserCreateForm, self).__init__(*args,**kwargs)        
        for fieldname in ['username','email','age', 'password1','password2']:           
            self.fields[fieldname].help_text = None            
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})