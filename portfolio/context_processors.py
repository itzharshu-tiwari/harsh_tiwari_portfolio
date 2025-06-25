from .models import SocialLink, Service

def connect_links(request):
    return {
        'connect_links': SocialLink.objects.all(),
        'services': Service.objects.all(),  
    }