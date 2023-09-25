from django.shortcuts import render, get_object_or_404
# Projemizin modellerini içe aktardık
from .models import Project, ProjectImage, Blogs
# Create your views here.


def home(request):
    projects = Project.objects.all()
    latest_blog_post = Blogs.objects.all()[1:4]

    return render(request, "home.html",{'projects': projects,'latest_blog':latest_blog_post})


def about(request):
    return render(request, "about-us.html")


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {'projects': projects})


def blogs(request):
    blogs = Blogs.objects.all()

    return render(request, "blogs.html", {"blogs": blogs})


def contact(request):
    return render(request, "contact.html")


def blog_detail(request, blog_slug):
    blog = get_object_or_404(Blogs, slug=blog_slug)
    return render(request, 'blog_detail.html', {'blog': blog})