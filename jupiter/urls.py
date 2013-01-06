from django.conf.urls import patterns, include, url

urlpatterns = patterns('jupiter.views',
        url(r'^$', 'index'),
)
