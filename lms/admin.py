from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Contact_us)

# admin.site.register(Author_Profile)
admin.site.site_title = 'Books Librarry'
admin.site.site_header = 'Books Librarry'