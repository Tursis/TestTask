from . import views
from django.conf.urls import include, url

app_name = 'blog'
urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^blogs/$', views.BlogListView.as_view(), name='blogs'),
 url(r'^bloggers/$', views.BloggerListView.as_view(), name='bloggers'),
  url(r'^(?P<pk>[0-9]+)/$', views.BlogDetailView.as_view(), name='blog-detail'),


]