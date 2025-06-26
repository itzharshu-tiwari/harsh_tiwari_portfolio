from django.contrib import admin
from .models import Contact
from .models import SocialLink
from .models import Service



# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
    ordering = ['-created_at']

# CONNECT
admin.site.register(SocialLink)

# SERVICES
admin.site.register(Service)


