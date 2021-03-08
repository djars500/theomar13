from django.contrib import admin
from .models import Category,Posts

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Posts)
# Register your models here.
