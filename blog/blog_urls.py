from django.urls import path
from blog import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('<int:blog_id>', views.detail, name='detail'),
]
