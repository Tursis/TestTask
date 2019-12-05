from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import BlogAuthor, Blog, BlogComment
from django.views.generic.edit import CreateView
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

class BloggersDetailView(generic.ListView):
	template_name = 'blog/blogauthor_detail.html'
	model = Blog

	def get_queryset(self):
		"""
		Return list of Blog objects created by BlogAuthor (author id specified in URL)
		"""
		id = self.kwargs['pk']
		target_author = get_object_or_404(BlogAuthor, pk=id)
		return Blog.objects.filter(author=target_author)

	def get_context_data(self,  **kwargs):
		context = super(BloggersDetailView, self).get_context_data(**kwargs)
		context['blogger'] = get_object_or_404(BlogAuthor, pk = self.kwargs['pk'])
		return  context

class BlogCommenetCreate(CreateView):
	model = BlogComment

	def get_context_data(self, **kwargs):
		context = super(BlogCommenetCreate, self).get_context_data(**kwargs)
		context['blogcomment'] = get_object_or_404(Blog, pk = self.kwargs['pk'])

	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.blog = get_object_or_404(Blog, pk = self.kwargs['pk'])
		return super(BlogCommenetCreate,self). form_valid(form)