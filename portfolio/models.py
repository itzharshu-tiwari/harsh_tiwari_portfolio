from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
# CONNECT 
class SocialLink(models.Model):
    platform = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100)  # like "bi bi-github"
    display_text = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)  # For LinkedIn, GitHub, etc.
    email = models.EmailField(blank=True, null=True)  # For Gmail link
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.platform

# SERVICES
class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, help_text="Example: 💻 or 🧪")

    def __str__(self):
        return f"{self.icon} {self.title}"


# HERO SECTION 
class HeroSection(models.Model):
    name = models.CharField(max_length=100)
    intro = models.TextField()
    profile_image = models.ImageField(upload_to='hero/')
    show_resume_button = models.BooleanField(default=True)
    show_contact_button = models.BooleanField(default=True)

    def __str__(self):
        return f"Hero Section - {self.name}"
    
# SKILL CARDS 
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='skills/')

    def __str__(self):
        return self.name
    
# CERTIFICATE
class Certificate(models.Model):
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    completed_date = models.CharField(max_length=100)
    image = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return self.title

# PROJECT
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')
    tech_stack = models.TextField(help_text="Use line breaks or commas to separate techs.")

    def __str__(self):
        return self.title


# RESUME 
class Resume(models.Model):
    profile = models.CharField(max_length=100)
    file = models.FileField(upload_to='resumes/')
    thumbnail = models.ImageField(upload_to='resume_thumbnails/', null=True, blank=True)  # 👈 for preview image

    def __str__(self):
        return self.profile