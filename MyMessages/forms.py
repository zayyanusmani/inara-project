from django import forms
from .models import Message, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'age']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.Select(attrs={'class': 'form-control'}),
        }

        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'content']