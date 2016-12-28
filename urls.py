from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from views import *
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smartcloud.views.home', name='home'),
    # url(r'^smartcloud/', include('smartcloud.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^site_static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    (r'^msg/', include('messages.urls')),
    (r'^proc/', include('envapply.urls')),
    url(r'^$',home),
    url(r'^login/',include('userManager.urls')),
    url(r'^forget_pwd/$','userManager.views.user.forgetPwd',name='forgetpwdurl'),
    url(r'^check_number/$','userManager.views.user.checkNumber',name='checknumurl'),
    url(r'^set_pwd/$','userManager.views.user.setPwd',name='setpwdurl'),
    url (r'^set_pwd_success/$', 'userManager.views.user.setPwdSuccess'),
    url(r'^admin/',include('userManager.urls')),
    url(r'^console/',include('userManager.urls')),
    url(r'^captcha/', include('captcha.urls')),
    (r'(.+\.html)$', getHtml),
)
