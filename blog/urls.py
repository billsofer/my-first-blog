
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_publish, name='post_publish'),
    url(r'^post/list$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),

]
