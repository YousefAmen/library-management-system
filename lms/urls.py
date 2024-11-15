from django.urls import path
from .views import *
urlpatterns = [
    
    path('',index, name = 'index'),
    path('<int:id>/',like_or_dislike, name = 'like_or_dislike'),
    path('books/',books,name = 'books'),
    path('card_book/<str:card_name>',card_book,name = 'book_card'),
    path('delete/<int:id_book>',delete,name = 'delete'),
    path('update/<int:id_book>',update,name = 'update'),
    path('contact us/',contact_us,name = 'contact_us'),
    
    
    
] 
