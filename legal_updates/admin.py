from django.contrib import admin
from .models import Legal,Events
# Register your models here.

class LegalAdmin(admin.ModelAdmin):
    search_fields = ['title']
    exclude = ('created_date',)
    prepopulated_fields = {'slug':('title',)}

class EventAdmin(admin.ModelAdmin):
    search_fields = ['title']
    exclude = ('created_date',)
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Legal,LegalAdmin)
admin.site.register(Events,EventAdmin)