from django import forms

from .models import Listing


class ListingCreationForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            "type",
            "title",
            "description",
            "price",
            "rate_unit",
            "subject",
            "category",
        ]
