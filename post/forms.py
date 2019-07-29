from django import forms
from .models import Post
class ReviewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'image','title', 'body'
        ]