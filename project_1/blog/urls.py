from django.urls import path
from .views import *

urlpatterns = [
    path('', post_lists, name="post_list_url"),
    path("post/<str:slug>/", post_detail, name="post_detail_url"),
    path("tags/", tag_lists, name="tags_list_url"),
    path("tags/<str:slug>/", tag_detail, name="tag_detail_url"),
]
