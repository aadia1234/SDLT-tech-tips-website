from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy



def SearchResults(request):
  if request.method == "POST":
    search_result = request.POST['search_result']
    posts = Post.objects.filter(title__contains=search_result)

    return render(request, 'search_results.html', {'search_result': search_result, 'posts': posts})
  else:
    return render(request, 'search_results.html', {})


def CategoryView(request, categories):
  category_posts = Post.objects.filter(category=categories.replace('-', ' '))
  return render(request, 'categories.html', {'categories': categories.title(), 'category_posts': category_posts})

class HomeView(ListView):
  model = Post
  template_name = 'home.html'
  ordering = ['-post_date']


class ArticleDetailView(DetailView):
  model = Post
  template_name = 'article_details.html'

class AddPostView(CreateView):
  model = Post
  template_name = 'add_post.html'
  form_class = PostForm

class AddCategoryView(CreateView):
  model = Category
  template_name = 'add_category.html'
  fields = '__all__'

class UpdatePostView(UpdateView):
  model = Post
  template_name = 'update_post.html'
  form_class = EditForm
  # fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
  model = Post
  template_name = 'delete_post.html'
  success_url = reverse_lazy('home')