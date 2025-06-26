from django.db import models

# CONTACT FORM
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# CONNECT SECTION
class SocialLink(models.Model):
    platform = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100)  # e.g. "bi bi-github"
    display_text = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.platform

# SERVICES SECTION
class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, help_text="Example: 💻 or 🧪")

    def __str__(self):
        return f"{self.icon} {self.title}"
