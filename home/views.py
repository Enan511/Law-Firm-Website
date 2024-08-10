from django.shortcuts import render,get_object_or_404
from .models import News

# Create your views here.
def home(request):
    news_articles = News.objects.all().order_by('-date_published')
    return render(request, 'index.html',{'news_articles':news_articles})
def news(request):
    return render(request, 'news-single.html')
def newsdetail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    recent_articles = News.objects.all().order_by('-date_published')[:5]
    context = {'news':news, 'recent_articles':recent_articles}
    return render(request, 'news-single.html', context)
def cart(request):
    return render(request, 'cart.html')
def all_news(request):
    news_articles = News.objects.all().order_by('-date_published')
    return render(request, 'allnews.html', {'news_articles': news_articles})
def upload_news(request):
    newsContent = News.objects.all()
    context = {'newsContent':newsContent}
    return render(request, 'addnews.html',context)
