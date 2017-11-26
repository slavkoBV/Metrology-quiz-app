from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^quiz_init', views.quiz_init, name='quiz_init'),
    url(r'^quiz_start', views.quiz_start, name='quiz_start'),
    url(r'^quiz_finish', views.quiz_finish, name='quiz_finish'),
]
