from django.urls import path
from . import views

urlpatterns = [
    path('', views.post.list, name='post_list')
]