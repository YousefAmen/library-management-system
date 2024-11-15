from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from lms.models import Book
from .forms import *
from .models import *


# registration user function
def registration_page(request):
  try:
    form = SignUpForm()
    if request.method  == "POST":
      form = SignUpForm(request.POST)
      if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username,password =password)
        login(request,user)
        return redirect('/')
        messages.success(request,f"Account Is Created Welcome {username}")
      else:
        messages.info(request,"Invalid Informations,Please Chack Your Details...")
        return redirect('registration')
    else:
      return render(request, 'registration/register.html',{'form':form})
  except :
    messages.info(request,"Error!!!")


# login user function
def login_user(request):
  if request.method =="POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request,username = username,password = password)
    if user is not None:
      login(request,user)
      messages.success(request,f"Login Successfully . Welcome Back {username}")
      return redirect('/')
    else:
      messages.info(request,f'This User Is Not Exists')
  else:
    return render(request,'registration/login.html')


# logout function
def logout_user(request):
  logout(request)
  messages.info(request,'Logged Out Successfully...')
  return redirect('/')
  return render(request,'registration/logout.html')


# profile page function
def profile_page(request):
  user_profile = Profile.objects.get(user=request.user)
  user_fav_books = Book.objects.filter(likes=user_profile.id)
  context = {'fav_books':user_fav_books}
  return render(request,'members_pages/profile.html',context)


# update profile function
def update_profile_page(request,id):
  user = Profile.objects.get(id=id)
  if request.method == "POST":
    update_profile = ProfileForms(request.POST,request.FILES,instance = user)
    if update_profile.is_valid():
      update_profile.save()
      messages.success(request,'Profile Is Updated Successfully')
      return redirect("/")
    else:
      messages.info(request,'Invalid Information !,Please Chack Your Details.')
  update_profile = ProfileForms(instance=user)
  context = {'forms':update_profile}
  return render(request,'members_pages/update_profile.html',context)


# writer profile function
def writer_profile(request,author_id):
  author = get_object_or_404(Author_Profile, id=author_id)
  book = Book.objects.filter(author=author)
  context = {'author_details':author,'author_books':book} 
  return render(request,'members_pages/writer.html',context)


# add wirter function
def add_writer(request):
  if request.method == 'POST':
    add_writer_forms = Author_Profile_Forms(request.POST,request.FILES)
    if add_writer_forms.is_valid():
      get_name = add_writer_forms.cleaned_data.get('writer_name')
      filter_the_name = Author_Profile.objects.filter(writer_name=get_name).exists()
      if not filter_the_name:
        add_writer_forms.save()
        messages.success(request,'Added Successfully.')
        return redirect('/')
      else:
        messages.info(request,'This Writer Is Already Exist')
    else:
      messages.info(request,'Invalid Information, PLease Chack Your Informations')
  context = {'add_writer_forms':Author_Profile_Forms}
  return render(request,'pages/add_writer.html',context)


# update writer profile function
def update_writer_profile(request,id):
  writer =Author_Profile.objects.get(id=id)
  if request.method == "POST":
    update_writer_profile = Author_Profile_Forms(request.POST,request.FILES,instance = writer)
    if update_writer_profile.is_valid():
      update_writer_profile.save()
      messages.success(request,'Author Profile Is Updated Successfully')
      return redirect("/")
    else:
      messages.info(request,'Invalid Information !,Please Chack Your Details.')
  else:
    update_writer_profile = Author_Profile_Forms(instance=writer)
  context = {'form':update_writer_profile}
  return render(request,'members_pages/update_writer_page.html',context)

