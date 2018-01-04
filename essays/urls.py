from django.conf.urls import url
from . import views

app_name = 'essays'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+).html$', views.post_detail, name='post_detail'),
    url(r'^category/(?P<pk>[0-9]+).html$', views.category, name='category'),
    url(r'^aboutme.html$', views.about, name='about'),
    url(r'^portfolio.html$', views.portfolio, name='portfolio'),
]   