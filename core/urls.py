from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from dashboard.views import AboutView, ContactView
from home import views as home_views
from jobs.views import (
    JobCreateView,
    JobDetailView,
    JobListView,
    accept_offer,
    submit_offer,
    take_job,
)
from listings import views as listings_views
from subscriptions import views as subscriptions_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_views.HomeView.as_view(), name="home"),
    path("accounts/", include("users.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("listings/", listings_views.ListingListView.as_view(), name="listings"),
    path(
        "listings/create/",
        listings_views.CreateListingView.as_view(),
        name="create-listing",
    ),
    path("jobs/", JobListView.as_view(), name="jobs"),
    path("jobs/create/", JobCreateView.as_view(), name="job-create"),
    path("jobs/<int:pk>/", JobDetailView.as_view(), name="job-detail"),
    path("jobs/<int:pk>/take/", take_job, name="job-take"),
    path("jobs/<int:pk>/offer/", submit_offer, name="job-offer"),
    path(
        "jobs/<int:job_id>/accept/<int:proposal_id>/",
        accept_offer,
        name="job-accept-offer",
    ),
    path("mentoring/", listings_views.MentorListView.as_view(), name="mentors"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("pricing/", subscriptions_views.PricingView.as_view(), name="pricing"),
    path(
        "pricing/change/<int:plan_id>/",
        subscriptions_views.change_plan,
        name="change-plan",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += debug_toolbar_urls()
