from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import poporiapp.views
import poporimember.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('poporiapp.urls')),
    path('poporimember/',include('poporimember.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)