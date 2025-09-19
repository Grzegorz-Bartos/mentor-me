from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import JobForm, ProposalForm
from .models import Job, Proposal


class JobListView(ListView):
    template_name = "job-list.html"
    model = Job
    context_object_name = "jobs"
    paginate_by = 9  # <- pagination

    def get_queryset(self):
        qs = super().get_queryset().order_by("-created_at")
        q = self.request.GET.get("q")
        mode = self.request.GET.get("mode")
        status = self.request.GET.get("status")
        if q:
            qs = qs.filter(
                Q(title__icontains=q)
                | Q(description__icontains=q)
                | Q(subject__icontains=q)
            )
        if mode in dict(Job.Mode.choices):
            qs = qs.filter(mode=mode)
        if status in dict(Job.Status.choices):
            qs = qs.filter(status=status)
        return qs


class JobCreateView(LoginRequiredMixin, CreateView):
    template_name = "job-create.html"
    form_class = JobForm
    model = Job
    success_url = reverse_lazy("jobs")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JobDetailView(DetailView):
    model = Job
    template_name = "course-details.html"


@login_required
def take_job(request, pk):
    job = get_object_or_404(
        Job, pk=pk, status=Job.Status.OPEN, mode=Job.Mode.FIRST_COME
    )
    if not request.user.can_take_jobs:
        messages.error(request, "Upgrade to Freelancer to take jobs.")
        return redirect("pricing")
    Proposal.objects.update_or_create(
        job=job, user=request.user, defaults={"is_accepted": True}
    )
    job.status = Job.Status.IN_PROGRESS
    job.save(update_fields=["status"])
    messages.success(request, "You have taken this job.")
    return redirect("jobs")


@login_required
def submit_offer(request, pk):
    job = get_object_or_404(Job, pk=pk, status=Job.Status.OPEN, mode=Job.Mode.OFFERS)
    if not request.user.can_take_jobs:
        messages.error(request, "Upgrade to Freelancer to submit offers.")
        return redirect("pricing")
    if request.method == "POST":
        form = ProposalForm(request.POST)
        if form.is_valid():
            Proposal.objects.update_or_create(
                job=job, user=request.user, defaults=form.cleaned_data
            )
            messages.success(request, "Offer submitted.")
            return redirect("jobs")
    else:
        form = ProposalForm()
    return render(request, "starter-page.html", {"form": form, "job": job})


@login_required
def accept_offer(request, job_id, proposal_id):
    job = get_object_or_404(Job, pk=job_id)
    if job.user != request.user:
        messages.error(request, "Only the job owner can accept offers.")
        return redirect("jobs")
    prop = get_object_or_404(Proposal, pk=proposal_id, job=job)
    Proposal.objects.filter(job=job).update(is_accepted=False)
    prop.is_accepted = True
    prop.save(update_fields=["is_accepted"])
    job.status = Job.Status.IN_PROGRESS
    job.save(update_fields=["status"])
    messages.success(request, "Offer accepted.")
    return redirect("jobs")
