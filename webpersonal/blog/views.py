from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
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
    if request.GET:
        searched = request.GET.get('searched', '').strip()
        title = request.GET.get('title', '').strip()
        tag = request.GET.get('tag', '').strip()
        date_from = request.GET.get('date_from', '')
        date_to = request.GET.get('date_to', '')

        posts = Post.objects.all()

        if searched:
            posts = posts.filter(
                Q(title__icontains=searched) |
                Q(description__icontains=searched) |
                Q(tags__category__icontains=searched)
            )
        if title:
            posts = posts.filter(title__icontains=title)
        if tag:
            posts = posts.filter(tags__category__iexact=tag)
        if date_from:
            posts = posts.filter(created_at__date__gte=date_from)
        if date_to:
            posts = posts.filter(created_at__date__lte=date_to)

        filtros = []
        if title:
            filtros.append(f"Título: {title}")
        if tag:
            filtros.append(f"Tag: {tag}")
        if date_from:
            filtros.append(f"Desde: {date_from}")
        if date_to:
            filtros.append(f"Hasta: {date_to}")

        if filtros:
            if searched:
                filtros.insert(0, f"Cualquier campo: {searched}")
            resumen = ", ".join(filtros)
        else:
            resumen = f"'{searched}'"

        return render(request, "blog/search_results.html", {
            'posts': posts.distinct(),
            'searched': searched,
            'title': title,
            'tag': tag,
            'date_from': date_from,
            'date_to': date_to,
            'has_filters': any([searched, title, tag, date_from, date_to]),
            'resumen': resumen,
            'all_tags': Tag.objects.order_by('category').values_list('category', flat=True),
        })
    else:
        return render(request, "blog/search_results.html", {})