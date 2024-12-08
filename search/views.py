from django.shortcuts import render
from authen.models import User
from chat.models import GroupChat

def search(request):
    query = request.GET.get('search', '')  # Get the search input from the request
    users = User.objects.filter(username__icontains=query) if query else []
    groups = GroupChat.objects.filter(group_username__icontains=query) if query else []  # Adjust field names as needed

    context = {
        'query': query,
        'users': users,
        'groups': groups,
    }
    return render(request, 'search/search.html', context)
