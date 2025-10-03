from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:slug>/', BlogPageView.as_view(), name='blog_post'),

    path('', BlogListView.as_view(), name='blog_list'),

    path('page/<int:page>/', BlogListView.as_view(), name='blog_list_paginated'),

    path('search/', BlogSearchView.as_view(), name='blog_search'),
]
