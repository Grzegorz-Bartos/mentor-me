from django.views.generic import ListView

from listings.models import Listing


class ListingListView(ListView):
    template_name = "listing_list.html"
    model = Listing
    context_object_name = "listings"


class JobsListView(ListView):
    template_name = "jobs_list.html"
    model = Listing
    context_object_name = "jobs"
