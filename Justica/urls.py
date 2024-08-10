from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('cart/',views.cart, name='cart'),
    # path('news/', views.news, name='news'),
    path('news/<int:news_id>', views.newsdetail, name='newsT'),
    path('all_news/', views.all_news, name='allnews'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)