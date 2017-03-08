from django.shortcuts import render_to_response
from django.template import RequestContext

from django import forms
from .models import NumImage

class ImagePostForm(forms.ModelForm):
    # owner = forms.CharField(max_length=20)
    class Meta:
        model = NumImage
        fields = ('image',)
