from django.urls import path
from django.views.generic import TemplateView

from main import views

app_name = 'main'
urlpatterns = [
    path("", views.home, name='home'),
    path("about-us/", views.about_us, name='about_us'),
    path("contact-us/", views.ContactUsView.as_view(), name="contact_us"),
    path("team/", views.team, name="team"),
    path("case-studies/", views.case_studies, name="case_studies"),
    path("careers/", views.careers, name="careers"),
    path("events/", views.events, name="events"),
]
