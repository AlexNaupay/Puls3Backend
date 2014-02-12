from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Puls3Backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','main.views.home'),
    url(r'^categoria/(?P<id_categoria>\d+)$','main.views.categoria'),
    url(r'^up/(?P<id_post>\d+)$','main.views.up'),
    url(r'^down/(?P<id_post>\d+)$','main.views.down'),
)
