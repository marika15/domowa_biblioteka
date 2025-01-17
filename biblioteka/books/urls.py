from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_book, name='add_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),

    path('borrowers/', views.borrower_list, name='borrower_list'),
    path('borrowers/add/', views.add_borrower, name='add_borrower'),
    path('borrowers/edit/<int:borrower_id>/', views.edit_borrower, name='edit_borrower'),
    path('borrowers/delete/<int:borrower_id>/', views.delete_borrower, name='delete_borrower'),

    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:category_id>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
]