from django.conf.urls import url
from blog import views
from django.urls import path

urlpatterns = [
    # path('time/',views.today_is, name='todays_time'),
    url(r'^time/$', views.today_is, name='todays_time'),
    url(r'^$', views.index, name='blog_index'),
]
