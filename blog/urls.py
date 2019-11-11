from . import views
from django.conf.urls import include, url

app_name = 'blog'
urlpatterns = [
 url('^$', views.index, name='index'),
 url('^blogs/$', views.BlogListView.as_view(), name='blogs'),
 url('^bloggers/$', views.BloggerListView.as_view(), name='bloggers'),
 url('^blogs/(?P<pk>[0-9]+)/$', views.BlogDetailView.as_view(), name='blog-detail'),
 url('^bloggers/(?P<slug>[\w.@+-]+)/$', views.BloggersDetailView.as_view(), name='bloggers-detail'),


]