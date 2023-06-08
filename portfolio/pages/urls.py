from django.urls import path

from portfolio.pages.views import HomeView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
]
