from django.db import models
from datetime import datetime
from members.models import Author_Profile
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
  category_name  = models.CharField(max_length=100, verbose_name='',default=None,unique=True,)
  
  def __str__(self):
    return self.category_name




class Book(models.Model):
  status_choices = [
  ('sold','Sold'),
  ('Rented','Rented'),
  ('Available','Available'),
  ]
  
  author             = models.ForeignKey(Author_Profile,on_delete=models.CASCADE,null=True)
  name               = models.CharField(max_length=100, verbose_name='',default=None,unique=True)
  # author_name        = models.CharField(max_length=100, null=True,blank=True,verbose_name='',default=None)
  image              = models.ImageField(upload_to = 'books_photos',null= True,blank = True)
  # author_image       = models.ImageField(upload_to = 'author_photos',null= True,blank = True,verbose_name='Author Image')
  status             = models.CharField(max_length=50,choices=status_choices,verbose_name='Book Status',default=None,null=True,blank=True)
  price              = models.DecimalField(max_digits=6,decimal_places=2,verbose_name='',null=True,blank=True,default=None)
  pages              = models.IntegerField(null=True,blank=True,verbose_name='',default=None)
  retal_price        = models.DecimalField(max_digits=6,null=True,blank=True,decimal_places=2,verbose_name='',default=None)
  retal_date         = models.DecimalField(max_digits=6,decimal_places=2,verbose_name='',default=None,null=True,blank=True)
  total_price        = models.DecimalField(max_digits=6,null=True,blank=True,decimal_places=2,verbose_name='',default=None)
  active             = models.BooleanField(default=True,)
  book_info          = models.TextField(max_length=500,verbose_name='',null=True,blank=True,default=None,)
  book_date          = models.DateField(null=True,blank=True,verbose_name='Book Puplishe Date')
  add_book_date      = models.DateTimeField(default=datetime.now)
  likes              = models.ManyToManyField(User,blank=True,related_name='book_likes')
  category           = models.ForeignKey(Category,on_delete=models.PROTECT,default=None,null=True,blank=True,verbose_name='Category')

  # make the name is title
  def save(self,*args,**kwargs):
    if self.name:
      self.name = self.name.title()
    super(Book,self).save(*args,**kwargs)


  # chack status
  def clean(self):
    if self.status == 'Rented':
      if self.price:
        raise ValidationError('Cannot Add Price in with Rentel Should be Use Rental Price of Day')
    else:
      if self.retal_price:
        raise ValidationError('Cannot Add Rental Price of Day with Sold Or Available Should be Use Price')

  # get how many likes in the book
  def number_of_likes(self):
    return self.likes.count()


  # return the name objects in the admin
  def __str__(self): 
    return self.name 
  


# contact us class hes included some filed to get 
class Contact_us(models.Model):
  custmoer_name          = models.CharField(max_length=50,verbose_name='',default=None,)
  custmoer_email         = models.EmailField(max_length=50,verbose_name='',default=None)
  message                = models.TextField(max_length=500,verbose_name='',default=None)


  def __str__(self):
    return self.custmoer_name


