from django import forms
from .models import GroupChat, GroupMessage

class CreateGroupChatForm(forms.ModelForm):
    class Meta:
        model = GroupChat
        fields = ['group_name', 'group_photo', 'group_username', 'description']
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Capture the user from kwargs
        super(CreateGroupChatForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        group_chat = super(CreateGroupChatForm, self).save(commit=False)
        if self.user:  # Ensure the user is set
            group_chat.creator = self.user
        if commit:
            group_chat.save()
            group_chat.members.add(self.user)  # Add the creator as a member
        return group_chat

class GroupMessageForm(forms.ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Type your message here...'
            }),
        }
    

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.group = kwargs.pop('group', None)
        super(GroupMessageForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        group_message = super().save(commit=False)
        group_message.sender = self.user
        group_message.group = self.group
        if commit:
            group_message.save()
        return group_message

class PrivateMessageForm(forms.ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Type your message here...'
            }),
        }
    
    def save(self, commit=True):
        private_message = super().save(commit=False)
        private_message.sender = self.user
        private_message.group = self.group
        if commit:
            private_message.save()
        return private_message
    