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
    paginate_by = 9  # <- pagination

    def get_queryset(self):
        qs = (
            super()
            .get_queryset()
            .select_related("user")
            .filter(type=Listing.ListingType.TUTOR, is_active=True)
            .order_by("-created_at")
        )
        q = self.request.GET.get("q")
        min_price = self.request.GET.get("min")
        max_price = self.request.GET.get("max")
        if q:
            qs = qs.filter(
                Q(title__icontains=q)
                | Q(description__icontains=q)
                | Q(subject__icontains=q)
                | Q(category__icontains=q)
            )
        if min_price:
            qs = qs.filter(price__gte=min_price)
        if max_price:
            qs = qs.filter(price__lte=max_price)
        return qs


class MentorListView(ListView):
    template_name = "mentor-list.html"
    model = Listing
    context_object_name = "listings"
    paginate_by = 9  # <- pagination

    def get_queryset(self):
        qs = (
            super()
            .get_queryset()
            .select_related("user")
            .filter(type=Listing.ListingType.MENTOR, is_active=True)
            .order_by("-created_at")
        )
        q = self.request.GET.get("q")
        min_price = self.request.GET.get("min")
        max_price = self.request.GET.get("max")
        if q:
            qs = qs.filter(
                Q(title__icontains=q)
                | Q(description__icontains=q)
                | Q(subject__icontains=q)
                | Q(category__icontains=q)
            )
        if min_price:
            qs = qs.filter(price__gte=min_price)
        if max_price:
            qs = qs.filter(price__lte=max_price)
        return qs


class CreateListingView(CapabilityRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = "create-listing.html"
    form_class = ListingCreationForm
    model = Listing
    success_url = reverse_lazy("listings")
    capability_name = None

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        selected_type = (
            self.request.POST.get("type")
            if self.request.method == "POST"
            else Listing.ListingType.TUTOR
        )
        self.capability_name = (
            "can_post_mentor"
            if selected_type == Listing.ListingType.MENTOR
            else "can_post_tutor"
        )
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
