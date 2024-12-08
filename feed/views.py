from django.shortcuts import render, redirect, get_object_or_404
from authen.models import User
from . forms import PostForm, CommentForm
from . models import Post, Comment
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def feed(request):

    user = request.user
    posts = Post.objects.all()
    for post in posts:
        post.comment_count = Comment.objects.filter(post=post).count()

    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'feed/feed.html', context)


@login_required
def like(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    if request.user in post.post_likes.all():
        post.post_likes.remove(request.user)
    else:
        post.post_likes.add(request.user)
    return JsonResponse({'likes': post.post_likes.count()})



@login_required
def bookmark(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    if request.user in post.post_bookmarks.all():
        post.post_bookmarks.remove(request.user)
    else:
        post.post_bookmarks.add(request.user)
    return JsonResponse({'bookmarks': post.post_bookmarks.count()})


@login_required
def comments(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-created_at')  # Order by latest comment first
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Set the post and user before saving
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('comments', post_id=post_id)  # Redirect back to the same post's comments
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form  # Pass the form to the template
    }

    return render(request, 'feed/comment.html', context)


@login_required
def create_post(request):
    form = PostForm()
        
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.instance.user = request.user  # Assign the current user to the post
            form.save()
            return redirect('feed')
    return render(request, 'feed/create-post.html', {'form': form})