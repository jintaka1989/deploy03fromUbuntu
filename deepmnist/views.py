# -*- coding: utf-8 -*-
from django.utils import timezone
# from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ImagePostForm
# from somewhere import handle_upload_file
# from django.core.files.uploadedfile import SimpleUploadedFile
from .models import NumImage

# Create your views here.
def deepmnist_gui(request):
    # import pdb; pdb.set_trace()
    return render(request, 'deepmnist/deepmnist_gui.html', {})

def deepmnist_new(request):
    if request.method == "POST":
        form = ImagePostForm(request.POST, request.FILES)
        request.session['a']="atest"
        request.session['b']="btest"

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
    else:
        form = ImagePostForm()
    return render(request, 'deepmnist/deepmnist_edit.html', {'form': form})

def recognize_view(request):
    if request.method == 'POST':
        if 'button_1' in request.POST:
            if request.session['test'] == None:
                a=1
            else:
                a=2
