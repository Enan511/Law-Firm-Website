from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comment
from .forms import NewsForm, CommentForm
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings


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

            # Send the thank you email
            send_mail(
                'Thank you for your comment',
                'Thanks for commenting on our post!',
                settings.DEFAULT_FROM_EMAIL,
                [comment.email],
                fail_silently=False,
            )

            return redirect('newsT', news_id=news_id)  # Redirect to avoid form resubmission
    else:
        form = CommentForm()
    recent_articles = News.objects.all().order_by('-date_published')[:5]
    context = {'news': news, 'recent_articles': recent_articles, 'comments': comments, 'form': form,
               'comment_count': comment_count}
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


def edit_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('newsT', news_id=news.id)
    else:
        form = NewsForm(instance=news)
    context = {'news': news, 'form': form}
    return render(request, 'edit_news.html', context)


def toggle_like(request, news_id):
    news = get_object_or_404(News, id=news_id)
    session_key = f'liked_{news_id}'

    if request.session.get(session_key, False):
        # User has already liked this post, so remove the like
        request.session[session_key] = False
        news.likes = max(news.likes - 1, 0)
        news.save()
        liked = False
    else:
        # User has not liked this post, so add the like
        request.session[session_key] = True
        news.likes += 1
        news.save()
        liked = True

    response = {
        'liked': liked,
        'total_likes': news.likes,
    }
    return JsonResponse(response)
