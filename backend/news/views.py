from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.contrib.auth.decorators import login_required

# CRUD
# - Create
# - Read
# - Update
# - Delete

def get_news(request):
    context = {
        "news": News.objects.all()
    }
    return render(request, "news.html", context)

@login_required
def create_news(request):
    context = { "form": NewsForm() }

    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('get_news')

    return render(request, "create_news.html", context)

@login_required
def update_news(request, pk: int):
    news = News.objects.get(pk=pk, author=request.user)
    context = {"form": NewsForm(instance=news)}

    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('get_news')

    return render(request, "update_news.html", context)

@login_required
def delete_news(request, pk: int):
    news = News.objects.get(pk=pk, author=request.user)
    news.delete()
    return redirect("get_news")
