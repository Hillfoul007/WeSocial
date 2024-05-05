from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('users.urls')),  # Include users.urls here
    path('profile/', include('users.urls')),   # Include users.urls here
    path('login/', include('users.urls')),     # Include users.urls here
    path('logout/', include('users.urls')),    # Include users.urls here
    path('', include('social.urls')),
    path('chat/', include('chat.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
