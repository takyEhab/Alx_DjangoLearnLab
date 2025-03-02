from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import register

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

from .views import admin_view
from .views import librarian_view
from .views import member_view

from .views import add_book
from .views import edit_book
from .views import delete_book

urlpatterns = [
    path('register/', register, name='register'),

    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    # views.register
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),
]

