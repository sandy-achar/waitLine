from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/(?P<prof>\w+)/(?P<student>\w+)/(?P<id>\w+)/$', views.add_to_list, name='add_to_list'),
    url(r'^delete/(?P<prof>\w+)/(?P<student>\w+)/$', views.delete_from_list, name='delete_from_list'),
    url(r'^prof/(?P<prof>\w+)/$', views.prof_list, name='prof_list'),
]


