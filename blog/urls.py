from django.urls import path
from .views import all_blogs, blog_detail

urlpatterns = [
    path('', all_blogs, name='all_blogs'),
    path('<int:blog_id>/', blog_detail, name='blog_detail'),
]
