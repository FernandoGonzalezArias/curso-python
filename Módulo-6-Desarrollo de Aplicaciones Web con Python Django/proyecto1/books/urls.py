from django.urls import path
from . import views


urlpatterns = [
    path ('', views.books_list),
    path('<int:pk>', views.book_detail),  #/book/id
    path('new', views.new_book)
    
]