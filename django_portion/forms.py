from django import forms
from django.core.validators import MaxLengthValidator
from .models import Comment
from django.utils.html import escape

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, validators=[MaxLengthValidator(500)])

    class Meta:
        model = Comment
        fields = ['name', 'body']

    def clean_body(self):
        body = self.cleaned_data['body']
        sanitized_body = escape(body)
        return sanitized_body
