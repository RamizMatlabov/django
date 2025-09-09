from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# CRUD
# - Create
# - Read
# - Update
# - Delete

class NewsView(ListView):
    model = News
    template_name = "news.html"
    context_object_name = "news"  # defaults to "object_list"




class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm  # This lets to use the form that we created inside templates
    template_name = 'create_news.html'
    success_url = '/news'

    # set request.user as an author of the post
    def form_valid(self, news):
        news.instance.author = self.request.user
        return super().form_valid(news)



class UpdateNewsView(UpdateView):
    model = News
    template_name = 'update_news.html'
    success_url = '/news'
    form_class = NewsForm


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news_confirm_delete.html'
    success_url = '/news'