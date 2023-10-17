from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = "easy_survey/home.html"


class SurveyAddView(TemplateView):
    template_name = "easy_survey/survey_add.html"
