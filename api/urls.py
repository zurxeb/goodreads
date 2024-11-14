from django.urls import path

from api import views
from api.views import BookReviewDetailAPIView, BookReviewListAPIView, BookDetailAPIView, BookListCreateAPIView

urlpatterns = [
    path('reviews/', BookReviewListAPIView.as_view(), name='reviews-list'),
    path('reviews/<int:id>/', BookReviewDetailAPIView.as_view(),name='reviews-detail'),
    path('books/', BookListCreateAPIView.as_view(), name='books-list'),
    path('books/<int:id>/', BookDetailAPIView.as_view(), name='books-detail'),


]
