from rest_framework import serializers

from books.models import BookReview,Book
from users.models import CustomUser




class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'isbn', 'cover_picture']

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username','email', 'first_name', 'last_name', 'profile_picture', 'gender']


class BookDetailSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    book = BookSerializers(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    book_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BookReview
        fields = ['id', 'stars_given','comment', 'created_at', 'book', 'user', 'book_id', 'user_id']