# middleware.py
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.deprecation import MiddlewareMixin


class DynamicSiteIDMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Get the host/domain from the request
        host = request.get_host().split(':')[0]  # Removes any port numbers
        
        # Query the Site model for matching domain
        try:
            site = Site.objects.get(domain=host)
            settings.SITE_ID = site.id
        except Site.DoesNotExist:
            # Optional: Set a default or raise an error if site not found
            settings.SITE_ID = 8  # Default SITE_ID, or handle as needed
