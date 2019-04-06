from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import PostItem


class PostItemListView(ListView):
    model = PostItem
    template_name = 'items/index.html'


class PostItemDetailView(DetailView):
    model = PostItem
    template_name = 'items/post_detail.html'


class PostItemCreateView(CreateView):
    model = PostItem
    fields = ['title', 'short_description',
              'description', 'post_category', 'post_image']
    template_name = 'items/new.html'

    # Get current user as author of post
    def form_valid(self, form):
        form.instance.user_post = self.request.user
        form.save()
        return super(PostItemCreateView, self).form_valid(form)
