from django.contrib import admin
from .models import Contact
from .models import Resume
from .models import HeroSection
from .models import Skill
from .models import Certificate
from .models import Project
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

# HERO
admin.site.register(HeroSection)

# SKILL
admin.site.register(Skill)

# CERTIFICATE
admin.site.register(Certificate)

# PROJECT
admin.site.register(Project)

# RESUME 
admin.site.register(Resume)
