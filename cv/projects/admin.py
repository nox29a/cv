from django.contrib import admin
from .models import Contact, Gallery, Skill, Memes


class GalleryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Skill)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Contact)
admin.site.register(Memes)
