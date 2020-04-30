"""Defining url patterns for faceboooks """
from django.urls import path, re_path
from . import views

# path( '', view.class , name= '')

urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    re_path(r'(?P<topic_id>\d+)/',views.topic,name='topic'),
    path('topics/new_topic', views.new_topic, name='new_topic'),
    re_path(r'new_entry/(?P<topic_id>\d+)', views.new_entry, name='new_entry'),
]
