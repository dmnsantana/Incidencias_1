from django.contrib import admin
from paginas.models import Page

# Register your models here.

class PagesAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "content",
        "slug",
        "visible",
        "created_at",
        "update_at",
    )

admin.site.register(Page,PagesAdmin)
