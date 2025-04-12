from django.views.generic import TemplateView


class PricingView(TemplateView):
    template_name = "pricing.html"
