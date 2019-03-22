from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

# Create your views here.
# def home(request):
#     blogs = Blog.objects
#     return render(request, 'blog/home.html', {'blogs': blogs})

def home(request):
    blogs = Blog.objects
    blog_list=Blog.objects.all()
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'blog/home.html',{'blogs':blogs,'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})