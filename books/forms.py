from django import forms

from books.models import Book, BookReview

from users.models import CustomUser

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'isbn', 'cover_picture')


class BookReviewForm(forms.ModelForm):
    stars_given = forms.IntegerField(max_value=5, min_value=1)
    class Meta:
        model = BookReview
        fields = ['stars_given', 'comment']





