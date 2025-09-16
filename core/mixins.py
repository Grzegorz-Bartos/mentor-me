from django.core.exceptions import PermissionDenied


class CapabilityRequiredMixin:
    capability_name: str = None  # e.g., 'can_post_tutor'

    def has_capability(self, user) -> bool:
        if not self.capability_name:
            return True
        return getattr(user, self.capability_name, False)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.contrib.auth.views import redirect_to_login

            return redirect_to_login(next=request.get_full_path())
        if not self.has_capability(request.user):
            raise PermissionDenied(
                "You don't have access to this action with your current plan."
            )
        return super().dispatch(request, *args, **kwargs)
