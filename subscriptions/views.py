from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from users.models import Account

from .models import Plan


class PricingView(TemplateView):
    template_name = "pricing.html"


@login_required
def change_plan(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    acc: Account = request.user
    acc.role_level = plan.level
    acc.save(update_fields=["role_level"])
    from .models import Subscription

    sub, _ = Subscription.objects.get_or_create(user=acc, defaults={"plan": plan})
    sub.plan = plan
    sub.is_active = True
    sub.save(update_fields=["plan", "is_active"])
    messages.success(request, f"Plan changed to {plan.name}.")
    return redirect("pricing")
