from django.contrib import admin
from jupiter.models import Post
from django import forms
from django.db import models

class PostAdmin(admin.ModelAdmin):
    #change_form_template = 'wysiwyg/admin/change_form.html'
    formfield_overrides = { models.TextField: {'widget':forms.Textarea(attrs ={'class':'ckeditor'})},}
    prepopulated_fields = {"slug":("title",)}

    class Media:
        js = ('ckeditor/ckeditor/ckeditor.js',)

admin.site.register(Post,PostAdmin)
