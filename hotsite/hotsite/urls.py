from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [
    url('^', include('hotsite.core.urls', namespace='core')),
    url('^panel/', include('hotsite.panel.urls', namespace='panel')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
