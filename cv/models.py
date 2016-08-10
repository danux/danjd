# ~*~ coding: utf-8 ~*~
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Skill(models.Model):
    """
    A skill has a name and a skill level.
    """
    name = models.CharField(max_length=30)
    skill_level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ['-skill_level']


class Job(models.Model):
    """
    A skill has a name and a skill level.
    """
    title = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ['-start_date']


class Project(models.Model):
    """
    A skill has a name and a skill level.
    """
    name = models.CharField(max_length=30)
    description = models.TextField()
    github_url = models.URLField()
    order = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ['order']
