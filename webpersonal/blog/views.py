from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, "blog/index.html", {
        'posts' : posts
        })
    
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/details.html',{'post': post})