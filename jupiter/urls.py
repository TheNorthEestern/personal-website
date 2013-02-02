from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template 
from django.views.generic import ListView, DetailView
from jupiter.models import Post
from tastypie.api import Api
from jupiter.api import PostResource

v1_api = Api(api_name="v1")
v1_api.register(PostResource())

urlpatterns = patterns('',
        url(r'^$',direct_to_template, {'template': 'static/index.html'}),
        url(r'^blog/$',ListView.as_view(queryset=Post.objects.all().order_by("-created")[:3],template_name='blog/blog.html')),
        url(r'^blog/(?P<slug>[-\w]+)$',DetailView.as_view(model=Post,template_name='blog/post.html')),
        url(r'^api/', include(v1_api.urls)),
)
