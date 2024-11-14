from django.urls import path

from books import views
from books.views import BookListView, BookDetailView, ReviewUpdateView

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<int:book_id>/', BookDetailView.as_view(), name='detail'),
    path('add/', views.add_book, name='add_book'),
    path('reviews/<int:pk>/edit/', ReviewUpdateView.as_view(), name='edit_review'),
    path('reviews/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('reviews/<int:review_id>/delete/', views.delete_review, name='delete_review'),
]

