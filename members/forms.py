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
  email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
  class Meta:
    model = User
    fields = ['username','email','password1','password2']
  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'User Name'
    self.fields['username'].label = ''
    self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    self.fields['password1'].label = ''
    self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    self.fields['password2'].label = ''
    self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
