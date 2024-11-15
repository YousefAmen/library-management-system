from django import forms
from .models import *


class Add_Category(forms.ModelForm):
  class Meta:
    model = Category
    fields = ['category_name']

    widgets = {
      'category_name':forms.TextInput(attrs={
        'class':'form-control',

      })
    }


# class book form to add book from the website
class Add_Book_Form(forms.ModelForm):

  class Meta:
    model = Book
    fields = [
    'author','name','image',
    'status','price','pages',
    'retal_date','retal_price',
    'total_price','category',
    'book_info','book_date','add_book_date','active',]
    widgets = {
      # author of book input
      'author':forms.Select(attrs={'class':'form-control'},),
      # name of book input
      'name':forms.TextInput(attrs={
      'class':'form-control',
      'placeholder':'Write The Book Name'
      }),
      # image of book input
      'image':forms.FileInput(attrs={'class':'form-control',}),
      # status of book input
      'status':forms.Select(attrs={'class':'form-control'}),
      'price':forms.NumberInput(attrs={
      'class':'form-control',
      'placeholder':'Book Price'
      }),
      # number of pages input
      'pages':forms.NumberInput(attrs={
        'class':'form-control',
      'placeholder':'Book Pages'
      }),
      # retal_price input
      'retal_price':forms.NumberInput(attrs={
      'class':'form-control',
      'id':'rental_price_day','placeholder':'Rental Price Of Day'
      }),
      # retal_date input
      'retal_date':forms.NumberInput(attrs={
      'class':'form-control',
      'id':'rental_date',
      'placeholder':'Rantal Days'
      }),
      # total price input
      'total_price':forms.NumberInput(attrs={
      'class':'form-control',
      'id':'total_price',
      'placeholder':'Total Rental Price'
      }),
      # book informations input
      'book_info':forms.Textarea(attrs={
      'class':'form-control',
      'placeholder':'Book Informations',
      }),
      # book_date input
      'book_date':forms.DateInput(attrs={
      'class':'form-control',
      'placeholder':'Year-Monthe-Day'
      }),
      # add_book_date input
      'add_book_date':forms.DateTimeInput(attrs={'class':'form-control'}),
      'category':forms.Select(attrs={'class':'form-control'}),
    }
    
    
    def clean(self):
      data = self.clean['price']
      if data is not None and data <= 0:
        raise forms.ValidationError("Rental price must be greater than zero.")
      return data
    def clean_rental_price(self):
        data = self.cleaned_data['retal_price']
        if data is not None and data <= 0:
            raise forms.ValidationError("Rental price must be greater than zero.")
        return data


class Contactus_forms(forms.ModelForm):
  class Meta:
    model =  Contact_us
    fields = "__all__"

    widgets={
    "custmoer_name":forms.TextInput(attrs={'placeholder':'Write Your Name','class':'form-control'}),
    "custmoer_email":forms.EmailInput(attrs={'placeholder':'Write Your Email','class':'form-control'}),
    "message":forms.Textarea(attrs={'placeholder':'Write Your Message','class':'form-control'}),
    
    }


