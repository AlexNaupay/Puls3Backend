from django.conf.urls import patterns, include, url

from django.contrib import admin
from main.views import HomeListView,PostDetailView
admin.autodiscover()

from django.views.generic import TemplateView

from main.views import PostViewSet,CategoriaViewSet
from rest_framework import routers
route = routers.DefaultRouter()
route.register(r'links',PostViewSet)
route.register(r'categoria',CategoriaViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Puls3Backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','main.views.home'),
    url(r'^categoria/(?P<id_categoria>\d+)$','main.views.categoria'),
    url(r'^up/(?P<id_post>\d+)$','main.views.up'),
    url(r'^down/(?P<id_post>\d+)$','main.views.down'),
    url(r'^home/$',TemplateView.as_view(template_name='index.html'),name='home'),
    url(r'^home2/$',HomeListView.as_view(),name='home2'),
    url(r'^post/(?P<pk>\d+)$',PostDetailView.as_view(),name='post'),
    url(r'^api/',include(route.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
