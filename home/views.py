from django.views.generic import TemplateView

from listings.models import Listing


class HomeView(TemplateView):
    template_name = "home.html"  # home.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["listings"] = Listing.objects.order_by("id")[:3]
        return context
