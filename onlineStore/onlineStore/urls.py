from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include(arg='cart.urls', namespace='cart')),
    path('user/', include(arg='users.urls', namespace='user')),
    path('orders/', include(arg='orders.urls', namespace='orders')),
    path('', include(arg='core.urls', namespace='core'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)