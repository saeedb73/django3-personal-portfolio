from django.shortcuts import render, get_object_or_404
from blog.models import Blogs


def blog_home(request):
    blogs = Blogs.objects.order_by('-date')

    return render(request, 'blog/blog_home.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
