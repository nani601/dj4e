from django.contrib import admin
from ads.models import Ad


# Define the PicAdmin class
class AdAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')


# Register your models here.
admin.site.register(Ad, AdAdmin)
