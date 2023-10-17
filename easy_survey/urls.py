from django.urls import path
from . import views

app_name = "easy_survey"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("survey/add", views.SurveyAddView.as_view(), name="add-survey"),
]
