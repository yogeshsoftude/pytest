from django.contrib import admin
from .models import Companies

# Register your models here.


@admin.register(Companies)
class CompnayAdmin(admin.ModelAdmin):
    pass
