from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.
from cv.models import Skill, Job, Project


class SkillTestCase(TestCase):
    """
    Basic tests of cv classs
    """
    def test_skill_cannot_be_over_100(self):
        skill = Skill(name='test', skill_level=101)
        self.assertRaises(
            ValidationError, skill.clean_fields, ['Ensure this value is less than or equal to 100.']
        )

    def test_skill_must_be_over_1(self):
        skill = Skill(name='test', skill_level=0)
        self.assertRaises(
            ValidationError, skill.clean_fields, ['Ensure this value is greater than or equal to 1.']
        )


class CvViewTestCase(TestCase):
    """
    Tests the CV view.
    """
    fixtures = ['initial_data.json']

    def test_view_renders(self):
        response = self.client.get(reverse('cv:cv'))
        self.assertEquals(200, response.status_code)
        self.assertEquals(list(Skill.objects.all()), list(response.context['skills']))
        self.assertEquals(list(Job.objects.all()), list(response.context['jobs']))
        self.assertEquals(list(Project.objects.all()), list(response.context['projects']))
        self.assertTemplateUsed(response, 'cv/cv.html')
