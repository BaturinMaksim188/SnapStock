from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('photos:photo_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photos/photo_list.html', {'photos': photos})

def photo_detail(request, id):
    photo = get_object_or_404(Photo, id=id)
    return render(request, 'photos/photo_detail.html', {'photo': photo})

@login_required
def photo_upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('photos:photo_detail', id=photo.id)
    else:
        form = PhotoForm()
    return render(request, 'photos/photo_upload.html', {'form': form})
