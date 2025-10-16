from django import forms

from .models import Listing


class ListingCreationForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title",
            "description",
            "price",
            "rate_unit",
            "subject",
            "category",
        ]
