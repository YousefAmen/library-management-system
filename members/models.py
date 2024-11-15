from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


# class users Profile
class Profile(models.Model):
  
  name              = models.CharField(max_length=100,default=None,null=True,verbose_name='')
  email             = models.EmailField(max_length=500,default=None,null=True,verbose_name='')
  profile_image     = models.ImageField(upload_to = 'author_photos',null= True,blank = True,verbose_name='Profile Image')
  bio               = models.TextField(max_length=300,default=None,null=True,verbose_name='')
  facebook_link     = models.CharField(max_length=300,null=True,blank=True,default=None,verbose_name='')
  instagram_link    = models.CharField(max_length=300,null=True,blank=True,default=None,verbose_name='')
  twitter_link      = models.CharField(max_length=300,null=True,blank=True,default=None,verbose_name='')
  linkedin_link     = models.CharField(max_length=300,null=True,blank=True,default=None,verbose_name='')
  user              = models.OneToOneField(User,null=True,on_delete=models.CASCADE,verbose_name='User')
  slug              = models.SlugField(verbose_name='Slug',null=True,blank=True)
  joined_date       = models.DateTimeField(default=datetime.now)


  def save(self,*args,**kwargs):
    if not self.slug:
      self.slug = slugify(self.user.username)
    super(Profile,self).save(*args,**kwargs)


  def __str__(self):
    return str(self.user.username)


# creating profile ever time user is signup
def creat_account(sender,**kwargs):
  if kwargs['created']:
    Profile.objects.create(user=kwargs['instance'])
post_save.connect(creat_account,sender = User)


# class Author Profile 
class Author_Profile(models.Model):
  writer_name        = models.CharField(max_length=100,default=None,verbose_name ='')
  writer_image       = models.ImageField(upload_to = 'author_photos',null= True,blank = True,verbose_name='Profile Image')
  writer_info        = models.TextField(max_length=500,default=None,blank=True,null=True,verbose_name ='')
  awardes            = models.CharField(max_length=500,null=True,blank=True,default=None,verbose_name ='')
  achievements       = models.CharField(max_length=500,null=True,blank=True,default=None,verbose_name ='')
  facebook_link      = models.CharField(max_length=500,null=True,blank=True,default=None,verbose_name ='')
  instagram_link     = models.CharField(max_length=500,null=True,blank=True,default=None,verbose_name ='')
  twitter_link       = models.CharField(max_length=500,null=True,blank=True,default=None,verbose_name ='')
  linkedin_link       = models.CharField(max_length=500,null=True,blank=True,default=None,verbose_name ='')


  # save function
  def save(self,*args,**kwargs):
    if self.writer_name:
      self.writer_name = self.writer_name.title()
    super(Author_Profile,self).save(*args,**kwargs)


  # str function
  def __str__(self):
    return self.writer_name