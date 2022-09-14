from django.contrib import admin
from django.urls import path, include
from django.conf import settings #add this
from django.conf.urls.static import static #add this

urlpatterns = [
    path('', include ('blog.urls')),
    path('admin/', admin.site.urls),
]

# #DEV ONLY
# if settings.DEBUG: 
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)