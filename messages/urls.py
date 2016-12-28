from django.conf.urls import patterns, url
from django_messages.views import *
from messages.forms import ComposeForm
from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='inbox/'), name='messages_redirect'),
    url(r'^compose/$',compose,{'form_class': ComposeForm,},name='messages_compose'),						          
    url(r'^inbox/$', inbox, name='messages_inbox'),
    url(r'^outbox/$', outbox, name='messages_outbox'),
    url(r'^compose/(?P<recipient>[\w.@+-]+)/$', compose, name='messages_compose_to'),
    url(r'^reply/(?P<message_id>[\d]+)/$', reply, name='messages_reply'),
    url(r'^view/(?P<message_id>[\d]+)/$', view, name='messages_detail'),
    url(r'^delete/(?P<message_id>[\d]+)/$', delete, name='messages_delete'),
    url(r'^undelete/(?P<message_id>[\d]+)/$', undelete, name='messages_undelete'),
    url(r'^trash/$', trash, name='messages_trash'),
)
