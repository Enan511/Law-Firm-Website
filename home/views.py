from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def news(request):
    return render(request, 'news-single.html')
def newsT(request, pk):
    return render(request, 'news-single.html', {'pk': pk})
def cart(request):
    return render(request, 'cart.html')
