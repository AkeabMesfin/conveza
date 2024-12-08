from django.shortcuts import render, get_object_or_404, redirect
from authen.models import User
from feed.models import Post
from chat.models import GroupChat, PrivateChat
from django.contrib.auth.decorators import login_required
from settings.forms import UserProfileUpdateForm
from feed.models import Comment
from django.http import JsonResponse
@login_required
def user_profile(request, id):
    groups = GroupChat.objects.filter(members=request.user)
    private_chats = PrivateChat.objects.filter(user1=request.user) | PrivateChat.objects.filter(user2=request.user)
    private_users = []
    for chat in private_chats:
        other_user = chat.user2 if chat.user1 == request.user else chat.user1
        private_users.append({'user': other_user, 'room_id': chat.room_id})


    current_user = request.user
    other_user = get_object_or_404(User, id=id)
    posts = Post.objects.filter(user=other_user).order_by('-created_at') 
    for post in posts:
        post.comment_count = Comment.objects.filter(post=post).count()
    groupchat = GroupChat.objects.filter(members=other_user).order_by('-created_at')

    return render(request, 'profile/user-profile.html', {
        'other_user': other_user, 
        'posts': posts, 
        'groupchat': groupchat,
        'current_user': current_user,
        'groups': groups,
        'private_users': private_users, 
    })

@login_required
def start_private_chat(request, id):
    # Get the other user
    other_user = get_object_or_404(User, id=id)

    # Check if the chat room already exists between the two users
    chat_room = PrivateChat.objects.filter(user1=request.user, user2=other_user).first() or \
                PrivateChat.objects.filter(user1=other_user, user2=request.user).first()

    # If no chat room exists, create a new one
    if not chat_room:
        chat_room = PrivateChat.objects.create(user1=request.user, user2=other_user)

    # Redirect to the private chat room
    return redirect('private-chat', room_id=chat_room.room_id)


def my_profile(request):
    user = request.user
    user_posts = Post.objects.filter(user=user).order_by('-created_at')  
    groups = GroupChat.objects.filter(members=request.user)
    for post in user_posts:
        post.comment_count = Comment.objects.filter(post=post).count()

    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('settings')  # Redirect to the same page or another page as needed
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = UserProfileUpdateForm(instance=user)


    return render(request, 'profile/my-profile.html', {
        'form': form,
        'user': user,
        'user_posts': user_posts,
        'groups': groups
    })

