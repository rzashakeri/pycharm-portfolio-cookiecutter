from django.core import validators
from django.db import models
from django.db.models import CASCADE


class SiteSettings(models.Model):
    domain = models.URLField()
    title = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.domain} | {self.title}"


class Page(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField()

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()


    def __str__(self):
        return self.title


class SkillCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    icon = models.ImageField()


class ContactUs(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(validators=[validators.validate_email])
    message = models.TextField()


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
