from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from books.models import BookReview

def landing_page(request):
    return render(request, 'landing_page.html')




class HomePageView(View):
    def get(self, request):
        reviews = BookReview.objects.all()


        paginator = Paginator(reviews, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
        }
        return render(request, 'home.html', context)






