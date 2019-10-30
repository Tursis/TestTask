from . import views
from django.conf.urls import include, url

app_name = 'blog'
urlpatterns = [
 url(r'^$', views.index, name='index'),

]