from django.shortcuts import render,get_object_or_404
from .models import News

# Create your views here.
def home(request):
    return render(request, 'index.html')
def news(request):
    return render(request, 'news-single.html')
def newsdetail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'news-single.html', {'news': news})
def cart(request):
    return render(request, 'cart.html')
def all_news(request):
    news_articles = News.objects.all().order_by('-date_published')
    return render(request, 'allnews.html', {'news_articles': news_articles})