from django.db import models

from users.models import Account


class Listing(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=50)  # ex. 'active', 'inactive'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
