from django.shortcuts import render, redirect
from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


from books.forms import BookCreateForm, BookReviewForm
from books.models import Book, BookReview


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        search = request.GET.get('q')
        if search:
            books = books.filter(title__icontains=search)

        paginator = Paginator(books, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
                'page_obj': page_obj,
                'books': books,
            }

        return render(request, 'list.html', context)


class BookDetailView(View):
    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        form = BookReviewForm
        reviews = BookReview.objects.filter(book=book)[::-1]
        context = {
            'book': book,
            'reviews': reviews,
            'form': form,


        }
        return render(request, 'detail.html', context)

    def post(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        form = BookReviewForm(request.POST)
        if form.is_valid():
            review = BookReview.objects.create(
                book=book,
                user=request.user,
                comment=form.cleaned_data['comment'],
                stars_given=form.cleaned_data['stars_given'],

            )

            review.save()
            return redirect('books:detail', book_id=book_id)
        context = {
            'form': form,
        }
        return render(request, 'detail.html', context)

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = BookReview
        form_class = BookReviewForm
        template_name = 'edit_book_reviews.html'
        context_object_name = 'review'


        def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)

        def get_success_url(self):
            return reverse_lazy('books:detail',
                                kwargs={'book_id': self.object.book.id})

        def test_func(self):
            review = self.get_object()
            return self.request.user == review.user
def edit_review(request, review_id):  
    review = get_object_or_404(BookReview, id=review_id, user=request.user)
    if request.method == "POST":
        form = BookReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('books:detail', book_id=review.book.id)
    else:
        form = BookReviewForm(instance=review)
    return render(request, 'edit_book_reviews.html', {'form': form})

def delete_review(request, review_id):
    review = get_object_or_404(BookReview, id=review_id, user=request.user)

    if request.method == "POST":
        review.delete()
        return redirect('books:detail', book_id=review.book.id)
    return render(request, 'delete_review.html', {'review': review})
def add_book (request):
    if request.method == 'POST':
        form = BookCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books:list')
    else:
        form = BookCreateForm()
    return render(request, 'add_book.html', {'form': form})


































