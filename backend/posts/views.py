from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# CRUD
# - Create
# - Read
# - Update
# - Delete


class PostsView(ListView):
    model = Posts
    template_name = "posts.html"
    context_object_name = "posts"  # defaults to "object_list"




class PostCreateView(CreateView):
    model = Posts
    form_class = PostsForm  # This lets to use the form that we created inside templates
    template_name = 'create_post.html'
    success_url = '/posts'

    # set request.user as an author of the post
    def form_valid(self, post):
        post.instance.author = self.request.user
        return super().form_valid(post)



class UpdatePostView(UpdateView):
    model = Posts
    template_name = 'update_post.html'
    success_url = '/posts'
    form_class = PostsForm


class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'post_confirm_delete.html'
    success_url = '/posts'