from django.urls import path
from . import views


urlpatterns = [
    path ('', views.books_list),
    path('<int:pk>', views.book_detail),  #/book/id
    path('new', views.new_book),         #/books/new
    path('<int:pk>/edit', views.edit_book),  #/books/id/edit
    path('<int:pk>/delete', views.destroy)
    
]