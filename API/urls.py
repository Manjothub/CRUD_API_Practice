from django.urls import path
from  .views import *

urlpatterns = [
    path('books/',books_collection,name="books"),
    path('addbook/',add_books_collection,name="addbooks")
]
 