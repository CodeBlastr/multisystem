from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Base urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Add static and media files handling in DEBUG mode
if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    # Include Debug Toolbar URLs
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

# Include Django CMS URLs
urlpatterns.append(path('', include('cms.urls')))

# Disable the admin navigation sidebar for better UX in Django CMS custom views
admin.site.enable_nav_sidebar = False
