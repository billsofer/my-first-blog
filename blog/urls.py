from django.conf.urls import url
from blog.views import post_list, post_detail

urlpatterns = [
    url(r'^$', post_list, name='post_new'),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='detail'),
]