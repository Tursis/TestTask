from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from  .models import BlogAuthor, Blog
# Create your views here.
def index(request):

	return render(request, 'index.html')

class BlogListView(generic.ListView):
	template_name = 'blog/blog_list.html'
	model = Blog

class BloggerListView(generic.ListView):
	template_name = 'blog/blogauthor_list.html'
	model = BlogAuthor



class BlogDetailView(generic.DetailView):
	model = Blog

class BloggersDetailView(generic.DetailView):
	model = BlogAuthor
	slug_field = 'user'

