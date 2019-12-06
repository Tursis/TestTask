from . import views
from django.conf.urls import include, url

app_name = 'blog'
urlpatterns = [
 url('^$', views.index, name='index'),
 url('^blogs/$', views.BlogListView.as_view(), name='blogs'),
 url('^bloggers/$', views.BloggerListView.as_view(), name='bloggers'),
 url('^blogs/(?P<pk>[0-9]+)/$', views.BlogDetailView.as_view(), name='blog-detail'),
 url('^bloggers/id(?P<pk>[0-9]+)$', views.BloggersDetailView.as_view(), name='bloggers-detail'),
 url('^blogs/(?P<pk>[0-9]+)/create',views.BlogCommenetCreate.as_view(),name='blog-comment')

]