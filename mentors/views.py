from django.views.generic import TemplateView


class MentorsListView(TemplateView):
    template_name = "mentors_list.html"
