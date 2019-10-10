from django.urls import path
import .views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs')
]
