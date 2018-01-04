import markdown
from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
from .models import Post, Category
from django.http import HttpResponse

# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', context={'post_list' : post_list})

def about(request):
    return render(request, 'aboutme.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk) 
    post_list = Post.objects.filter(category=cate).order_by('-created_at')
    return render(request, 'index.html', context={'post_list' : post_list})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    post.content = markdown.markdown(post.content, extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                    ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'post.html', context=context)