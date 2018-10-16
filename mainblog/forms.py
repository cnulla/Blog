from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text','cover_image', 'category', 'tag']

        widgets = {
                "title": forms.TextInput(attrs={'class': 'form-control'}),
                "text": forms.Textarea(attrs={'class': 'form-control'}),
        }

