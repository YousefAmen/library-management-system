from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q


# function index page
def index(request):
  # add books
  if request.method == 'POST':
    add_book = Add_Book_Form(request.POST,request.FILES)
    if add_book.is_valid():
      add_book.save()
    # add category in the index page
    add_category = Add_Category(request.POST)
    if request.method == 'POST':
      if add_category.is_valid():
        add_category.save()
  book_objects = Book.objects.all()
  
  books_number  = Book.objects.count()
  context = {
      'books':book_objects ,
      'category':Category.objects.all(),
      'count':books_number,
      'book_form':Add_Book_Form(),
      'add_category':Add_Category(),
      'status_sold': book_objects.filter(status='sold').count(),
      'status_available':book_objects.filter(status='Available').count(),
      'status_rented':book_objects.filter(status='Rented').count(),
      }  
  return render(request,'pages/index.html',context)


# like or dislike function
def like_or_dislike(request,id):
  get_like=get_object_or_404(Book,id=id)
  if get_like.likes.filter(id=request.user.id):
      get_like.likes.remove(request.user)
  else:
    get_like.likes.add(request.user)
  page_redirect = request.META.get("HTTP_REFERER")
  return redirect(page_redirect)


# function books page
def books(request):
  # search logic
  book = Book.objects.all()
  search = None
  if "search_name" in request.GET:
    search_term = request.GET["search_name"]
    if search_term:
      search = book.filter(Q(name__icontains = search_term)|Q(book_info__icontains=search_term))
    
  # aad category logic in the books page
  add_category = Add_Category(request.POST)
  if request.method == 'POST':
    if add_category.is_valid():
      add_category.save()
  else:
      add_category = Add_Category()
  # context 
  books = Book.objects.all()
  context = {
  "books":search,
  "all_books":books,
  'category':Category.objects.all(),
  "add_category":Add_Category()
  }
  return render(request,'pages/books.html',context)


# function delete page
def delete(request,id_book):
  get_delete_book = get_object_or_404(Book ,id=id_book)
  if request.method =="POST":
    delete_book = get_delete_book.delete()
    return redirect("/")
  return render(request,'pages/delete.html',)


# function update pagebook
def update(request,id_book):
  get_id_book = Book.objects.get(id =id_book)
  if request.method == "POST":
    book_forms = Add_Book_Form(request.POST,request.FILES,instance=get_id_book)
    if book_forms.is_valid():
      save_book = book_forms.save() 
      return redirect("/")
  else:
    book_forms = Add_Book_Form(instance=get_id_book)
  context = {'form':book_forms}
  return render(request,'pages/update.html',context)


# book card function
def card_book(request,card_name):
  book = Book.objects.get(name=card_name)
  related_books=Book.objects.filter(category=book.category).exclude(id=book.id)
  all_books=Book.objects.all()
  context = {
    'book_card':book,
    'books':related_books,
    'all_books':all_books,
    }
  return render(request,'pages/card_book.html',context)


# contect us function
def contact_us(request):
  if request.method=='POST':
    message = Contactus_forms(request.POST)
    if message.is_valid():
      save_message=message.save()
  context = {
    'contact_form':Contactus_forms
    }
  return render(request,'pages/contact_us.html',context)
