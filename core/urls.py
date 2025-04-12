from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from dashboard import views as dashboard_views
from home import views as home_views
from listings import views as listings_views
from subscriptions import views as subscriptions_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_views.HomeView.as_view(), name="home"),
    path("accounts/", include("users.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("listings/", listings_views.ListingListView.as_view(), name="listings"),
    path("jobs/", listings_views.JobsListView.as_view(), name="jobs"),
    path("mentoring/", listings_views.MentorListView.as_view(), name="mentors"),
    path("about/", dashboard_views.AboutView.as_view(), name="about"),
    path("contact/", dashboard_views.ContactView.as_view(), name="contact"),
    path("pricing/", subscriptions_views.PricingView.as_view(), name="pricing"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += debug_toolbar_urls()
