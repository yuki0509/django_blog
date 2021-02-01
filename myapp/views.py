from django.shortcuts import render, resolve_url
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from . models import Post
from django.urls import reverse_lazy
from . forms import PostForm
from django.contrib import messages


# Create your views here.
class Index(TemplateView):
    template_name = 'myapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_list = Post.objects.all()
        context = {
            'post_list': post_list,
        }
        return context

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('myapp:index')

class PostDetail(DetailView):
    model = Post

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        messages.success(self.request, 'Postを更新しました。')
        return resolve_url('myapp:post_detail', pk=self.kwargs['pk'])

class PostDelete(DeleteView):
    model = Post

    def get_success_url(self):
        messages.success(self.request, 'Postを削除しました。')
        return resolve_url('myapp:index')

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(state=1).order_by('-created_at')
