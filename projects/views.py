import requests
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Gallery, Skill, Memes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def skill_view(request):
    skills = Skill.objects.all()
    context = {"skills": skills}
    return render(request, "base.html", context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)

def project_gallery(request):
    gallery = Gallery.objects.order_by('-years')
    context = {"projects": (gallery)}
    return render(request, "project_gallery.html", context)

def project_detail(request, pk):
    gallery = Gallery.objects.get(pk=pk)
    context = {"project": gallery}
    return render(request, "project_detail.html", context)

def project_memes(request):
    memes = Memes.objects.all()
    context = {"memes": memes}
    return render(request, "project_memes.html", context)

def project_instagram(request):
    return render(request, "project_instagram.html")

def project_video(request):
    return render(request, "project_video.html")

def project_counter(request):
    return render(request, "project_counter.html")

def project_snake(request):
    return render(request, "project_snake.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('base')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)

def bored(request):

        url = f'https://www.boredapi.com/api/activity'
        response = requests.get(url, verify=False)
        data = response.json()
        activity = data['activity']

        context = {
            'activity' : activity
        }
        return render(request, 'project_api_bored.html', context)