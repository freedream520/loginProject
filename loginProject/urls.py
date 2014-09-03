from django.conf.urls import patterns, include, url

urlpatterns = patterns('pessas.views',
    url(r'^$', 'index'),
    url(r'^login/$', 'login'),
    url(r'^validar/$', 'validar'),
    url(r'^logoff/$', 'logoff'),
    url(r'^dashboard/$', 'dashboard'),
    url(r'^cadastro/$', 'cadastro'),

)
