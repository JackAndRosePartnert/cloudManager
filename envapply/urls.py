from django.conf.urls import patterns, include, url

urlpatterns = patterns('envapply.views',
    url(r'^env/apply$', 'envproc.applyEnv', name='applyenvurl'),
    url(r'^env/applylist$', 'envproc.listApply', name='listapplyurl'),
    url(r'^env/approvedlist$', 'envproc.listApproved', name='listapprovedurl'),
    url(r'^env/approve/(?P<ID>\d+)/(?P<status>\d+)/$', 'envproc.approve', name='approveurl'),

)
