from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(pages_patterns)),
    path('admin/', admin.site.urls),
    # path de auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
