from django.urls import path
from . import views

urlpatterns = [
    path("gallery", views.project_gallery, name="gallery"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("memes", views.project_memes, name="memes"),
    path("bot", views.project_instagram, name="bot"),
    path("snake", views.project_snake, name="snake"),
    path("video", views.project_video, name="video"),
    path("counter", views.project_counter, name="counter"),
    path('contact', views.contact_view, name='contact'),
    path('register', views.register, name='register'),
    path('bored', views.bored, name='bored'),
    path('', views.skill_view, name='base'),


]