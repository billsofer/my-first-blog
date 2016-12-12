from django.conf.urls import url
from classes.views import classes_list, classes_detail

urlpatterns = [
    url(r'^$', classes_list, name='classes'),
    url(r'(?P<pk>\d+)/$', classes_detail, name='class'),
]