from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm
from django.db.models import Q

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, "blog/index.html", {
        'posts' : posts
        })
    
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect('blog:detail', slug=slug)
    
    else:
        form = CommentForm()
    
    return render(request, 'blog/details.html', {
                'post': post,
                'form': form})

def search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts= Post.objects.filter(Q(title__contains=searched) | Q(description__contains=searched) | Q(tags__category__contains=searched)) #dps veo como poner los tags
        return render(request, "blog/search_results.html", {'searched': searched, 'posts' : posts})
    else:
        return render(request, "blog/search_results.html", {})