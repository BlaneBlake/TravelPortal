"""
URL configuration for TravelPortal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('Authentication.urls', 'Authentication'), 'Authentication')),
    path('', include(('Blog.urls', 'Blog'), 'Blog')),
    path('set_language/', set_language, name='set_language'),
] + static(settings.STATIC_URL)

# if settings.DEBUG:: Upewniamy się, że pliki multimedialne są serwowane tylko w trybie developerskim, gdy DEBUG=True.
# W środowisku produkcyjnym serwowanie plików statycznych i multimedialnych powinno być obsługiwane przez serwer WWW,
# taki jak nginx lub Apache.

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)