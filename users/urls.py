from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/(?P<prof>\w+)/(?P<student>\w+)/(?P<id>\w+)/$', views.add_to_list, name='add_to_list'),
]


