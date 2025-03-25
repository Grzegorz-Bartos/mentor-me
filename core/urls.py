from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path

from core import settings

urlpatterns = [
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
