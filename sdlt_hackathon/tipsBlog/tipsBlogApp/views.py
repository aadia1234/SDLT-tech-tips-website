from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
  model = Post
  template_name = 'home.html'
  ordering = ['-post_date']

  # def get_context_data(self, *args, **kwargs):
  #   category_menu = Category.objects.all()
  #   context = super(HomeView, self).get_context_data(*args, **kwargs)
  #   context["category_menu"] = category_menu
  #   return context


def CategoryView(request, categories):
  category_posts = Post.objects.filter(category=categories.replace('-', ' '))
  return render(request, 'categories.html', {'categories': categories.title(), 'category_posts': category_posts})

class ArticleDetailView(DetailView):
  model = Post
  template_name = 'article_details.html'
  
  # def get_context_data(self, *args, **kwargs):
  #   category_menu = Category.objects.all()
  #   context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
  #   context["category_menu"] = category_menu
  #   return context

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
