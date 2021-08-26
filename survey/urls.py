from django.urls import path
from .views import (
                    HomeView, CreateSurvey, SurveyDetails,  SurveyView, UpdateSurvey,
                   
    )

app_name = "survey"

urlpatterns = [
    path('', HomeView.as_view(), name = 'home-page'),
    path('survey/', CreateSurvey.as_view(), name= 'survey-page'),
    path('viewsurvey/', SurveyView.as_view(), name= 'survey-view'),
    path('<str:code>/survey-detail/', SurveyDetails.as_view(), name = 'survey-detail'),
    path('<str:code>/survey/update/', UpdateSurvey.as_view(), name = 'survey-update'),

    
]