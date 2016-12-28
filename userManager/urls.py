from django.conf.urls import patterns, include, url

urlpatterns = patterns('userManager.views',
    url(r'^$', 'user.login', name='loginurl'),
    url(r'^logout/$', 'user.logoutUser', name='logouturl'),

    url(r'^user/add/$', 'user.addUser', name='adduserurl'),
    url(r'^user/list/$', 'user.listUser', name='listuserurl'),
    url(r'^user/edit/(?P<ID>\d+)/$', 'user.editUser', name='edituserurl'),
    url(r'^user/delete/(?P<ID>\d+)/$', 'user.deleteUser', name='deleteuserurl'),
    url(r'^user/changepwd/$', 'user.changePassword', name='changepwdurl'),

    url(r'^company/add/$', 'company.addCompany', name='addcompanyurl'),
    url(r'^company/list/$', 'company.listCompany', name='listcompanyurl'),
    url(r'^company/edit/(?P<ID>\d+)/$', 'company.editCompany', name='editcompanyurl'),
    url(r'^company/delete/(?P<ID>\d+)/$', 'company.deleteCompany', name='deletecompanyurl'),
    
    url(r'^permission/add/$', 'permission.addPermission', name='addpermissionurl'),
    url(r'^permission/list/$', 'permission.listPermission', name='listpermissionurl'),
    url(r'^permission/edit/(?P<ID>\d+)/$', 'permission.editPermission', name='editpermissionurl'),
    url(r'^permission/delete/(?P<ID>\d+)/$', 'permission.deletePermission', name='deletepermissionurl'),
#    url(r'^user/resetpwd/(?P<ID>\d+)/$', 'user.ResetPassword', name='resetpasswordurl'),

    url(r'^role/list/$', 'role.listRole', name='listroleurl'),
    url(r'^role/edit/(?P<ID>\d+)/$', 'role.editRolePermission', name='editrolepermissionurl'),

#    url(r'^permission/deny/$', 'permission.NoPermission', name='permissiondenyurl'),
    url(r'^userinfo/$', 'user.getUserinfo', name='userinfourl'),

)
