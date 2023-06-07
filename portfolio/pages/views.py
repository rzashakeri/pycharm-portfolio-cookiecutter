from django.shortcuts import render
from django.views import View

from portfolio.pages.models import SiteSettings, Page


class HomeView(View):
    def get(self, request):
        page = Page.objects.first()
        portfolio = SiteSettings.objects.first()
        context = {
            "page": page,
            "portfolio": portfolio
        }
        return render(request, "pages/index.html", context=context)
