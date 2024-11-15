from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BookDetailSerializers, BookSerializers
from books.models import BookReview, Book


class BookListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializers
class BookReviewDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookDetailSerializers(book_review)

        return Response(serializer.data, )

    def delete(self, request, id):
        book_review = BookReview.objects.get(id=id)
        book_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request, id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookDetailSerializers(instance=book_review,data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookDetailSerializers(instance=book_review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # json_data = {
        #     'id': book_review.id,
        #     'comment': book_review.comment,
        #     'created_at': book_review.created_at,
        #     'stars_given': book_review.stars_given,
        #     'book': {
        #         'id': book_review.book.id,
        #         'title': book_review.book.title,
        #         'description': book_review.book.description,
        #         'isbn': book_review.book.isbn,
        #     },
        #     'user': {
        #         'id': book_review.user.id,
        #         'username': book_review.user.username,
        #         'first_name': book_review.user.first_name,
        #         'last_name': book_review.user.last_name,
        #         'email': book_review.user.email,
        #     }
        # }
        # return JsonResponse(json_data)





class BookReviewListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        book_reviews = BookReview.objects.all().order_by('-created_at')
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(book_reviews, request)
        serializer = BookDetailSerializers(page_obj, many=True)
        return paginator.get_paginated_response(serializer.data)


    def post(self, request):
        serializer = BookDetailSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BookDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookSerializers(book)

        return Response(serializer.data, )

    def delete(self, request, id):
        book = Book.objects.get(id=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookSerializers(instance=book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookSerializers(instance=book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        book = Book.objects.all()
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(book, request)
        serializer_class = BookSerializers(page_obj, many=True)
        return paginator.get_paginated_response(serializer_class.data)


    def post(self, request):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


