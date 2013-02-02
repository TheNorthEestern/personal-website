from tastypie.resources import ModelResource
from jupiter.models import Post

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
