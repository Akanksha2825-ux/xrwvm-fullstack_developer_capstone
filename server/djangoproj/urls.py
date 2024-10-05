from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Admin path
    path('admin/', admin.site.urls),

    # Include app-specific URLs
    path('djangoapp/', include('djangoapp.urls')),

    # Home page
    path('', TemplateView.as_view(template_name="Home.html")),

    # About page
    path('about/', TemplateView.as_view(template_name="About.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
