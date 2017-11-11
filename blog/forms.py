from django import forms
from .models import Post
from .models import UserComment

class PostForm (forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ('user','comment',)