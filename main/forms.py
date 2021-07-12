from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Forum, Discussion
from django import forms

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={
                'required': True,
                'placeholder': 'abcd@example.com',
                'autofocus': True
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'abcxyz',
            })
        }

     	
    def __init__(self, *args, **kwargs):
       	super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs = {'placeholder': 'password'}
        self.fields['password2'].widget.attrs = {'placeholder': 'confirm password'}

class LoginForm(AuthenticationForm):
	class Meta:
		fields = '__all__'

class NewForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['topic', 'description']
        widgets = {
        	'topic':forms.TextInput(attrs={
        		'autofocus': True,
        		})
        }

class NewDiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['answer']

class NewReplyForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['answer']
        widgets = {
            'answer': forms.Textarea(attrs={
                'rows' : 2,
                'placeholder': 'What are your thoughts?'
                })
        }
   		