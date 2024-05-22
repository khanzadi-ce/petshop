from django.contrib import admin
from .models import Pet, Species


# Register your models here.
admin.site.register(Species)
admin.site.register(Pet)

