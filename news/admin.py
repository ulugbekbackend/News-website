from django.contrib import admin

from .models import Category,News,Contact
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display=['title','category','publish_time','status']
    list_filter=['status','publish_time','created_time']
    prepopulated_fields={'slug':('title',)}
    date_hierarchy='publish_time'
    search_fields=['title','body']
    ordering=['status','publish_time']

# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title']
    
admin.site.register(Category,CategoryAdmin)


admin.site.register(Contact)