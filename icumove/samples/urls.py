from django.conf.urls import url

from . import views

urlpatterns = [
    #  ex: /samples/
    url(r'^$', views.index, name='index'),
    # ex: /samples/air/
    url(r'^air/$', views.air_index, name='air index'),
    # ex: /samples/air/[UID]
    url(r'^air/(?P<uid>[^/]+)', views.air_detail, name='air detail'),
    # ex: /samples/stool/
    url(r'^stool/$', views.stool_index, name='stool index'),
    # ex: /samples/stool/[UID]
    url(r'^stool/(?P<uid>[^/]+)', views.stool_detail, name='stool detail'),
    # ex: /samples/door/
    url(r'^door/$', views.door_index, name='door index'),
    # ex: /samples/door/[UID]
    url(r'^door/(?P<uid>[^/]+)', views.door_detail, name='door detail'),
    # ex: /samples/floor/
    url(r'^floor/$', views.floor_index, name='floor index'),
    # ex: /samples/floor/[UID]
    url(r'^floor/(?P<uid>[^/]+)', views.floor_detail, name='floor detail'),
    # ex: /samples/date/[date]
    url(r'^date/(?P<date>[^/]+)', views.date_view, name='date detail'),
]