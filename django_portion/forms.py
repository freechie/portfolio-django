from django import forms
from django.core.validators import MaxLengthValidator
from .models import Comment
from django.utils.html import escape
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea, validators=[
                           MaxLengthValidator(50)])
    body = forms.CharField(widget=forms.Textarea, validators=[
                           MaxLengthValidator(500)])
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['name', 'body', 'captcha']

    def clean_body(self):
        body = self.cleaned_data['body']
        sanitized_body = escape(body)
        return sanitized_body
