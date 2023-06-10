from django.urls import path

from portfolio.pages.views import HomeView, AboutView, ContactUsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home/', HomeView.as_view()),
    path('about-us/', AboutView.as_view(), name='about'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
]
