from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib import messages
from .forms import UserProfileUpdateForm
from feed.models import Post
from chat.models import GroupChat
from authen.models import User
from feed.models import Comment, Post
from django.db.models import Count

# Create your views here.


@login_required
def settings(request):
    user = request.user
    user_posts = Post.objects.filter(user=user).order_by('-created_at')  
    groups = GroupChat.objects.filter(members=request.user)

    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('settings')  # Redirect to the same page or another page as needed
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = UserProfileUpdateForm(instance=user)

    return render(request, 'settings/settings.html', {
        'form': form,
        'user': user,
        'user_posts': user_posts,
        'groups': groups
    })


@login_required
def liked_saved_post(request):
    user = request.user

    # Fetch liked and bookmarked posts
    liked_posts = Post.objects.filter(post_likes=user).annotate(comment_count=Count('comments')).order_by('-created_at')
    bookmarked_posts = Post.objects.filter(post_bookmarks=user).annotate(comment_count=Count('comments')).order_by('-created_at')

    return render(request, 'settings/liked-saved-post.html', {
        'liked_posts': liked_posts,
        'bookmarked_posts': bookmarked_posts,
    })
