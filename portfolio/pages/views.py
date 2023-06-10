from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from portfolio.pages.models import SiteSettings, Page, About


class HomeView(View):
    def get(self, request):
        home = Page.objects.get(slug="home")
        context = {
            "page": home,
        }
        return render(request, "pages/index.html", context=context)


class AboutView(View):
    def get(self, request):
        about = About.objects.first()
        context = {
            "page": about
        }
        return render(request, "pages/about.html", context=context)


class SideBarView(TemplateView):
    template_name = "shared/sidebar.html"
    ordering = ['is_parent']

    def get_context_data(self, **kwargs):
        pages = Page.objects.all().order_by("-is_parent", "title")
        kwargs['pages'] = pages
        return super(SideBarView, self).get_context_data(**kwargs)


def render_navbar_title(request):
    portfolio = SiteSettings.objects.first()
    context = {
        "portfolio": portfolio
    }
    return render(request, "shared/partials/navbar_title.html", context=context)


def breadcrumb_title(request):
    portfolio = SiteSettings.objects.first()
    context = {
        "portfolio": portfolio
    }
    return render(request, "shared/partials/breadcrumb_title.html", context=context)
