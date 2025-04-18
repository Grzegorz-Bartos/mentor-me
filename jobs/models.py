from django.db import models

from users.models import Account


class Job(models.Model):
    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="jobs",
        help_text="User's account",
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()  # -> DecimalField (max_digtis, decimal_places)
    category = models.CharField(max_length=100)  # choice field
    status = models.CharField(max_length=50)  # ex. 'active', 'inactive' -> choicefield
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
