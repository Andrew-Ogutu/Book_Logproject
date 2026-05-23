from django.urls import path
from . import views
app_name = 'Book_logs'

urlpatterns =[

    #Home page
    path('',views.index, name='index'),
    path('Books/',views.Books, name='Books'),
    path('Books/<int:Book_id>/',views.BookDetail, name='BookDetail'),
    path('new_Book/',views.new_Book, name='new_Book'),

]