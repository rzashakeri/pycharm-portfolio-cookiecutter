import datetime

from django.core import validators
from django.db import models
from django.db.models import CASCADE


class SiteSettings(models.Model):
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.domain} | {self.name}"


class Page(models.Model):
    title = models.CharField(max_length=200)
    icon = models.FileField(upload_to="icons/")
    slug = models.SlugField(max_length=300)
    parent = models.ForeignKey("Page", on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_parent = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class About(Page):
    heading = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.heading


class SkillCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Skill(Page):
    category = models.ForeignKey(SkillCategory, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField()

    def __str__(self):
        return f"{self.name} ({self.category})"


class ContactUs(Page):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(validators=[validators.validate_email])
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.email} | Time: {self.created_on}"


class Project(Page):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
