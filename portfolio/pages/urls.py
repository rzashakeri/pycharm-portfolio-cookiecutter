from django.urls import path

from portfolio.pages.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='Home')
]
