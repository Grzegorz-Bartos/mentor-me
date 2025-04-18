from django.views.generic import ListView

from .models import Job


class JobListView(ListView):
    template_name = "job-list.html"
    model = Job  # add separate model
    context_object_name = "jobs"
