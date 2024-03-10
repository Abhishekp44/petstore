from django.contrib import admin

# Register your models here.
from petstoreapp.models import Pet
# register model pet by decorator
#@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display=('id','name','gender','species','breed','age','description')
    list_filter=['gender','age']
admin.site.register(Pet,PetAdmin)