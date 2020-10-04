from django.contrib import admin
from .models import Pet

# Register your models here.


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'age', 'adoption_date', 'weight', 'height', 'details', 'deleted')


admin.site.register(Pet, PetAdmin)
