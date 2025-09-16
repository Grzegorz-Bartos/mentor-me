from django.conf import settings
from django.db import models
from django.utils import timezone


class Listing(models.Model):
    class ListingType(models.TextChoices):
        TUTOR = "tutor", "Tutor"
        MENTOR = "mentor", "Mentor"

    class RateUnit(models.TextChoices):
        HOURLY = "hourly", "per hour"
        FIXED = "fixed", "fixed"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="listings"
    )
    type = models.CharField(
        max_length=10, choices=ListingType.choices, default=ListingType.TUTOR
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rate_unit = models.CharField(
        max_length=10, choices=RateUnit.choices, default=RateUnit.HOURLY
    )
    subject = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_type_display()}: {self.title}"
