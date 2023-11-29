from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('Home.urls')),
    # ... your other urlpatterns ...
]

# Add this only during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add a URL pattern for the root path
urlpatterns += [
    path('', include('Home.urls')),  # Include app-level URLs for the root path
]
