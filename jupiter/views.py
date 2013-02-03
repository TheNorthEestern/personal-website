from jupiter.models import Post
from django.shortcuts import render_to_response
from django.http import HttpResponse

def tags(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("blog/tags.html", {'posts':posts, 'tag':tag})

def index(request):
    return HttpResponse("Houston, we have liftoff")
