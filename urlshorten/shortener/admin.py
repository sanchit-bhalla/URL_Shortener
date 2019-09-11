from django.contrib import admin
from .models import Url
# Register your models here.
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id','http_url','publish_date', 'count')
    ordering = ('-publish_date',)
 
admin.site.register(Url, UrlsAdmin)