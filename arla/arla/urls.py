
from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static

from core.views import index, contact

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('item/', include('item.urls')),
    path('category/', include('category.urls')),
    path('cart/', include('cart.urls')),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)