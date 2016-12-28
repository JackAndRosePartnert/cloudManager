from django.conf.urls import patterns, include, url

urlpatterns = patterns('hello.views',
    url(r'^getImage/$', 'hello'),
)


