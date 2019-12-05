from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class BlogAuthor(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	bio = models.TextField(max_length=400, help_text="Enter your bio details here.")
	

	def get_absolute_url(self):
		return reverse('blog:bloggers-detail', args=[str(self.id)])

	def __str__(self):
		return self.user.username


class Blog(models.Model):
	name = models.CharField(max_length=200, help_text="Enter your name blog here.")
	author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
	description = models.TextField(max_length=400, help_text="Enter your blog text here.")
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:blog-detail', args=[str(self.id)])

class BlogComment(models.Model):
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	description = models.TextField(max_length=400, help_text='Enter your comment here')
	blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
	pub_date = models.DateTimeField('date published')

	class Meta:
		ordering = ['pub_date']

	def __str__(self):
		"""
		String for representing the Model object.
		"""
		len_title = 75
		if len(self.description) > len_title:
			titlestring = self.description[:len_title] + '...'
		else:
			titlestring = self.description
		return titlestring
