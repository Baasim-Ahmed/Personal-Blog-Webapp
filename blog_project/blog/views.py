from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import BlogPostForm
from .forms import CommentForm

def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', slug=slug)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })


@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})

# View to display all blog posts
def post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# View to display a single post
def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

# Create your views here.
