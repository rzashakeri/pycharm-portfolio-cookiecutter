from django.contrib import admin

from portfolio.pages.models import Page, About, SkillCategory, Skill, ContactUs, Project

admin.site.register(Page)
admin.site.register(About)
admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(ContactUs)
admin.site.register(Project)
