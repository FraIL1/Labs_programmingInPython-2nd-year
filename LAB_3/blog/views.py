from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator

def post_list(request):
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    # обработка поиска
    query = request.GET.get('q')
    if query:
        posts_list = posts_list.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query)
        )
    
    # пагинация 5 постов на страницу
    paginator = Paginator(posts_list, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        if author and text:
            Comment.objects.create(post=post, author=author, text=text)
            return redirect('post_detail', pk=post.pk)
    
    return render(request, 'blog/post_detail.html', {'post': post})

def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category, published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})