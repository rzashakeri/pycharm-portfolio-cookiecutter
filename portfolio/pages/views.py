from django.shortcuts import render
from django.views import View

from portfolio.pages.models import SiteSettings, Page, About


class HomeView(View):
    def get(self, request):
        page = Page.objects.get(title="index.html")
        portfolio = SiteSettings.objects.first()
        context = {
            "page": page,
            "portfolio": portfolio
        }
        return render(request, "pages/index.html", context=context)


class AboutView(View):
    def get(self, request):
        page = Page.objects.get(title="about.html")
        portfolio = SiteSettings.objects.first()
        about = About.objects.first()
        context = {
            "page": page,
            "portfolio": portfolio,
            "about": about
        }
        return render(request, "pages/about.html", context=context)
