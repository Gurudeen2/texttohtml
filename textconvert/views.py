from django.shortcuts import render
from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(),label="Text Editor")
    class Meta:
        model=Post
        fields=('body',)

def home(request):
    form=PostForm()
    return render(request,'base.html',{'form':form})