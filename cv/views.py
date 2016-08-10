# ~*~ coding: utf-8 ~*~
from django.views.generic import TemplateView

from cv.models import Skill, Job, Project


class CvTemplateView(TemplateView):
    template_name = 'cv/cv.html'

    def get_context_data(self, **kwargs):
        context_data = super(CvTemplateView, self).get_context_data(**kwargs)
        context_data['skills'] = Skill.objects.all()
        context_data['jobs'] = Job.objects.all()
        context_data['projects'] = Project.objects.all()
        return context_data
