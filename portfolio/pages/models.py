from django.db import models
from django.db.models import CASCADE


class Page(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField()


class About(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()


class SkillCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    icon = models.ImageField()
