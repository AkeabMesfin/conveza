from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateGroupChatForm, GroupMessageForm, PrivateMessageForm
from django.contrib.auth.decorators import login_required
from .models import GroupChat, GroupMessage, PrivateMessage, PrivateChat


@login_required
def chat(request):
    groups = GroupChat.objects.filter(members=request.user)
    private_chats = PrivateChat.objects.filter(user1=request.user) | PrivateChat.objects.filter(user2=request.user)
    private_users = []
    for chat in private_chats:
        other_user = chat.user2 if chat.user1 == request.user else chat.user1
        private_users.append({'user': other_user, 'room_id': chat.room_id})

    return render(request, 'chat/chat.html', {
        'groups': groups,
        'private_users': private_users,  # Pass the list of users with room IDs
    })


@login_required
def create_group(request):
    user = request.user
    if request.method == 'POST':
        form = CreateGroupChatForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('feed')  # Replace with your redirect URL
    else:
        form = CreateGroupChatForm(user=request.user)
    return render(request, 'chat/create-group.html', {'form': form, 'user': user})

@login_required
def group_chat(request, group_id):
    group = get_object_or_404(GroupChat, group_id=group_id)
    messages = GroupMessage.objects.filter(group=group).order_by('timestamp')
    groups = GroupChat.objects.filter(members=request.user)
    private_chats = PrivateChat.objects.filter(user1=request.user) | PrivateChat.objects.filter(user2=request.user)
    private_users = []
    for chat in private_chats:
        other_user = chat.user2 if chat.user1 == request.user else chat.user1
        private_users.append({'user': other_user, 'room_id': chat.room_id})

    # Handle message form submission
    if request.method == 'POST':
        form = GroupMessageForm(request.POST, user=request.user, group=group)
        if form.is_valid():
            form.save()
            return redirect('group-chat', group_id=group_id)  
    else:
        form = GroupMessageForm(user=request.user, group=group)

    return render(request, 'chat/group-chat.html', {
        'group': group,
        'messages': messages,
        'form': form,
        'groups': groups,
        'private_users': private_users,  
    })

@login_required
def group_detail(request, group_id):
    group = get_object_or_404(GroupChat, group_id=group_id)
    members = group.members.all()
    groups = GroupChat.objects.filter(members=request.user)
    private_chats = PrivateChat.objects.filter(user1=request.user) | PrivateChat.objects.filter(user2=request.user)
    private_users = []
    for chat in private_chats:
        other_user = chat.user2 if chat.user1 == request.user else chat.user1
        private_users.append({'user': other_user, 'room_id': chat.room_id})

    return render(request, 'chat/group-detail.html', {'group': group, 'members': members, 'groups': groups, 'private_users': private_users})

@login_required
def leave_group(request, group_id):
    group = get_object_or_404(GroupChat, group_id=group_id)
    if request.user in group.members.all():
        group.members.remove(request.user)
    return redirect('chat')

@login_required
def join_group(request, group_id):
    group = get_object_or_404(GroupChat, group_id=group_id)
    
    if request.user not in group.members.all():  
        group.members.add(request.user)
        return redirect('group-detail', group_id=group.group_id)  
    elif request.user in group.members.all():
        return redirect('group-chat', group_id=group.group_id)

    return redirect('group-chat', group_id=group.group_id)  


@login_required
def private_chat(request, room_id):

    groups = GroupChat.objects.filter(members=request.user)

    private_chats = PrivateChat.objects.filter(user1=request.user) | PrivateChat.objects.filter(user2=request.user)

    private_users = []
    for chat in private_chats:
        other_user = chat.user2 if chat.user1 == request.user else chat.user1
        private_users.append({'user': other_user, 'room_id': chat.room_id})


    chat_room = get_object_or_404(PrivateChat, room_id=room_id)
    messages = PrivateMessage.objects.filter(chat=chat_room).order_by('timestamp')  # Oldest to newest

    if request.method == 'POST':
        form = PrivateMessageForm(request.POST)
        if form.is_valid():
            PrivateMessage.objects.create(
                chat=chat_room,
                sender=request.user,
                content=form.cleaned_data['content']
            )
            return redirect('private-chat', room_id=room_id)
    else:
        form = PrivateMessageForm()

    # Render the template with chat messages and the message form
    return render(request, 'chat/private-chat.html', {
        'room_id': room_id,
        'chat_room': chat_room,
        'messages': messages,
        'form': form,
        'groups': groups,
        'private_users': private_users,
    })


