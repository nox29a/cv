from django.db import models

class Year(models.IntegerChoices):
    Year2020 = 2020
    Year2021 = 2021
    Year2022 = 2022
    Year2023 = 2023


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    years = models.IntegerField(choices=Year.choices)
    image = models.ImageField(upload_to='assets/img/gallery')
    def __str__(self):
        return self.title

class Memes(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assets/img/memes')
    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    def __str__(self):
        return self.email

class Skill(models.Model):
    name = models.CharField(max_length=30)
    value = models.IntegerField()
    def __str__(self):
        return self.name

