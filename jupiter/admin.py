from django.contrib import admin
from jupiter.models import Post
from django import forms
from django.db import models
from astronomica.settings import STATIC_URL
import os

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'

class PostAdmin(admin.ModelAdmin):
    #change_form_template = 'wysiwyg/admin/change_form.html'
    formfield_overrides = { models.TextField: {'widget':forms.Textarea(attrs ={'class':'ckeditor'})},}
    prepopulated_fields = {"slug":("title",)}

    class Media:
        js = ( AWS_URL + 'ckeditor/ckeditor/ckeditor.js',)

admin.site.register(Post,PostAdmin)
