from django.contrib import admin
from core.models import Acronym

admin.site.site_header = "Honeywell Acronym App Administration"

# Register your models here.
admin.site.register(Acronym)