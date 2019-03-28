from django.conf.urls import url
from blog import views
from django.urls import path

urlpatterns = [
    # path('time/',views.today_is, name='todays_time'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name="post_by_tag"),
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.post_by_category, name="post_by_category"),
    url(r'^$', views.post_list, name="post_list"),
    url(r'(?P<pk>^\d+)/$', views.post_detail, name='post_detail'),
]
