from django import forms
from .models import Post, Category, Tag

class PostForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects, widget=forms.CheckboxSelectMultiple(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'text','cover_image', 'category', 'tag']

        widgets = {
                "title": forms.TextInput(attrs={'class': 'form-control'}),
                "text": forms.Textarea(attrs={'class': 'form-control'}),
                # "category": forms.ChoiceField(attrs={'class': 'form-control'}),
        }

class TagForm(forms.ModelForm):

        class Meta:
            model = Tag
            fields = ['tag_input']
