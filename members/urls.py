from django.urls import path
from .views import *

urlpatterns = [
    
    path('profile_page/',profile_page,name = 'profile'),
    path('profile_page/<int:id>',update_profile_page,name = 'update_profile'),
    path('Add_writer/',add_writer,name = 'add_writer'),
    path('writer/<int:author_id>',writer_profile,name = 'writer_page'),
    path('writer/update/<int:id>', update_writer_profile, name='update_writer_profile_page'),  
    path('registration/',registration_page, name='registration'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
]  
