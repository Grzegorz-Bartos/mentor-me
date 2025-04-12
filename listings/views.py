from django.views.generic import ListView

from listings.models import Listing


class ListingListView(ListView):
    template_name = "listings.html"
    model = Listing
    context_object_name = "listings"


class JobsListView(ListView):
    template_name = "job-list.html"
    model = Listing
    context_object_name = "jobs"


class MentorListView(ListView):
    template_name = "mentor-list.html"
    model = Listing
