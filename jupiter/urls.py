from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template 
from django.views.generic import ListView, DetailView
from jupiter.models import Post

urlpatterns = patterns('',
        url(r'^$',direct_to_template, {'template': 'static/index.html'}),
        url(r'^blog/$',ListView.as_view(queryset=Post.objects.all().order_by("-created")[:2],template_name='blog/blog.html')),
        url(r'^blog/(?P<slug>[-\w]+)$',DetailView.as_view(model=Post,template_name='blog/post.html')),
)
