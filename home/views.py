from django.shortcuts import render, get_object_or_404, redirect
from .models import News,Comment
from .forms import NewsForm,CommentForm


# Create your views here.
def home(request):
    news_articles = News.objects.all().order_by('-date_published')
    return render(request, 'index.html', {'news_articles': news_articles})


def news(request):
    return render(request, 'news-single.html')


def newsdetail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    comments = news.comments.all()
    comment_count = comments.count()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.save()
            return redirect('newsT', news_id=news_id)  # Redirect to avoid form resubmission
    else:
        form = CommentForm()
    recent_articles = News.objects.all().order_by('-date_published')[:5]
    context = {'news': news, 'recent_articles': recent_articles, 'comments': comments, 'form': form, 'comment_count': comment_count}
    return render(request, 'news-single.html', context)


def cart(request):
    return render(request, 'cart.html')


def all_news(request):
    news_articles = News.objects.all().order_by('-date_published')
    return render(request, 'allnews.html', {'news_articles': news_articles})


def upload_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(all_news)
        else:
            print(form.errors)
    return render(request, 'addnews.html', {'form': NewsForm})
