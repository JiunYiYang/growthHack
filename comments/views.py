from django.shortcuts import render, get_object_or_404, redirect
from essays.models import Post
# Create your views here.

from essays.models import Comment
from .forms import CommentForm

def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)

        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'post.html', context=context)

    return redirect(post)
