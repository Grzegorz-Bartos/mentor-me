from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from core.mixins import CapabilityRequiredMixin

from .forms import ListingCreationForm
from .models import Listing


class ListingListView(ListView):
    template_name = "listings.html"
    model = Listing
    context_object_name = "listings"

    def get_queryset(self):
        qs = (
            super()
            .get_queryset()
            .filter(type=Listing.ListingType.TUTOR, is_active=True)
        )
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(title__icontains=q)
                | Q(description__icontains=q)
                | Q(subject__icontains=q)
            )
        return qs


class MentorListView(ListView):
    template_name = "mentor-list.html"
    model = Listing
    context_object_name = "listings"

    def get_queryset(self):
        qs = (
            super()
            .get_queryset()
            .filter(type=Listing.ListingType.MENTOR, is_active=True)
        )
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(title__icontains=q)
                | Q(description__icontains=q)
                | Q(subject__icontains=q)
            )
        return qs


class CreateListingView(CapabilityRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = "create-listing.html"
    form_class = ListingCreationForm
    model = Listing
    success_url = reverse_lazy("listings")
    capability_name = None

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == "POST":
            selected_type = self.request.POST.get("type")
        else:
            selected_type = Listing.ListingType.TUTOR
        if selected_type == Listing.ListingType.MENTOR:
            self.capability_name = "can_post_mentor"
        else:
            self.capability_name = "can_post_tutor"
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
