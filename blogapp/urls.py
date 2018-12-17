from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexview),
    url(r'^page/(\d+)$', views.indexview),
    url(r'^post/(\d+)$', views.detailview),
    url(r'^category/(\d+)$', views.article_view),
    url(r'^archive/(\d+)/(\d+)$', views.archive_view),
    url(r'^archive/$', views.archive_view),
]
