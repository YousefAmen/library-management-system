from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class ProfileForms(forms.ModelForm):
  class Meta:
    model = Profile
    fields = [
    'name',
    'email',
    'profile_image',
    'bio',
    'facebook_link',
    'instagram_link',
    'twitter_link',]

    widgets={
      'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Write Your Name'}),
      'email':forms.TextInput(attrs={'class':'form-control','placeholder':'example@gmail.com'}),
      'profile_image':forms.FileInput(attrs={'class':'form-control'}),
      'bio':forms.Textarea(attrs={'placeholder':'Write an overview of yourself (The number of words should not exceed 300)','class':'form-control'}),
      'facebook_link':forms.TextInput(attrs={'placeholder':'Writer Facebook Link','class':'form-control'}),
      'instagram_link':forms.TextInput(attrs={'placeholder':'Writer Instegram','class':'form-control'}),
      'twitter_link':forms.TextInput(attrs={'placeholder':'Writer Twitter Link','class':'form-control'}),
    }

class  Author_Profile_Forms(forms.ModelForm):
  class Meta:
    model = Author_Profile
    fields = ['writer_name','writer_image','writer_info','awardes','achievements','facebook_link','instagram_link','twitter_link']
    widgets={
      'writer_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Writer Name'}),
      'writer_image':forms.FileInput(attrs={'class':'form-control','placeholder':'Writer Image'}),
      'writer_info':forms.Textarea(attrs={'class':'form-control','placeholder':'Writer Informations'}),
      'awardes':forms.TextInput(attrs={'class':'form-control','placeholder':'Writer Awardas'}),
      'achievements':forms.TextInput(attrs={'class':'form-control','placeholder':'Writer achievements (optional)'}),
      'facebook_link':forms.TextInput(attrs={'class':'form-control','placeholder':'Facebook Link (optional)',}),
      'instagram_link':forms.TextInput(attrs={'class':'form-control','placeholder':'Instegram (optional)',}),
      'twitter_link':forms.TextInput(attrs={'class':'form-control','placeholder':'Twitter Link (optional)'}),
    }
  
class SignUpForm(UserCreationForm):
  email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'form-control'}))
  class Meta:
    model = User
    fields = ['username','email','password1','password2']

# class Login_Forms(forms.Form):
#   username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Write Your Name','class':'form-control'})),
#   password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Write Your Password','class':'form-control'})),