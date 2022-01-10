from django.contrib import admin
from django.urls import path
from django.views.static import serve
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FLUTTER_WEB_APP = os.path.join(BASE_DIR, 'flutter_web_app')

def flutter_redirect(request, resource):
    return serve(request, resource, FLUTTER_WEB_APP)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flutter_web_app/', lambda r: flutter_redirect(r, 'build/web/index.html')),
    path('flutter_web_app/<path:resource>', flutter_redirect)
]
