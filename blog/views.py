from django.core.paginator import Paginator
from django.shortcuts import redirect
from .forms import NewsForms
from django.views.generic import  DetailView
from .models import News, Category
from django.shortcuts import render


def index(request):
    search_list = request.GET.get('search','')

    if search_list:
        news = News.objects.filter(
            title__icontains=search_list
        )
    else:
        news = News.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(news,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    content = {
        'blog': news,
        'categories': categories,
        'page_obj': page_obj,
    }
    return render(
        request,
        'blog/home.html',
        context=content
    )

def get_category(request, category_id):
    news = News.objects.filter(
        category_id=category_id
    )
    categories = Category.objects.all()
    category = Category.objects.get(
        pk=category_id
    )
    paginator = Paginator(news, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    content = {
        'blog': news,
        'categories': categories,
        'category': category,
        'page_obj': page_obj,
    }
    return render(
        request,
        'blog/category.html',
        context=content
    )

class Show_one(DetailView):
    template_name = 'blog/one_news.html'
    model = News

def addpage(request):
    if request.method == 'POST':
        form = NewsForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = NewsForms
    return render(
        request,
        'blog/new_news.html',
        context={'form':form}
    )





