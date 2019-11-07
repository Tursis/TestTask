from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class BlogAuthor(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	bio = models.TextField(max_length=400, help_text="Enter your bio details here.")


	def get_absolute_url(self):
		return reverse('blog:bloggers', args=[str(self.id)])

	def __str__(self):
		return self.user.username


class Blog(models.Model):
	name = models.CharField(max_length=200, help_text="Enter your name blog here.")
	author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
	description = models.TextField(max_length=400, help_text="Enter your blog tex here.")
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:blog-detail', args=[str(self.id)])
