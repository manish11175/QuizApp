
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import	settings
from django.conf.urls.static import	static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz_api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/',obtain_auth_token),
    
]
if	settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
