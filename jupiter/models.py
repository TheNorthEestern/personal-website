import datetime
from django.db import models
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = HTMLField()
    created = models.DateTimeField(editable=False)
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
