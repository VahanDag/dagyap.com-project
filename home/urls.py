from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us', views.about, name="about-us"),
    path('projects', views.projects, name="projects"),
    path('blogs', views.blogs, name="blogs"),
    path('contact', views.contact, name="contact"),
    path('blog/<slug:blog_slug>/', views.blog_detail, name='blog-detail'),

]