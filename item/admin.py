from django.contrib import admin
from item.models import Item,Review

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'image')

admin.site.register(Item, ItemAdmin)
admin.site.register(Review)
