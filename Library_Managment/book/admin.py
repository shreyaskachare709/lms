from django.contrib import admin
from .models import BookTable

# Register your models here.
@admin.register(BookTable)
class BookTableAdmin(admin.ModelAdmin):
    list_display=['id','book_name','author_name', 'price' ,'typeofbook','is_deleted']
