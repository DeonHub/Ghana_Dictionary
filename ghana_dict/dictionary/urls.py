from django.urls import path
from dictionary.views import *


urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('english/', EnglishWordView.as_view(), name='english'),
    path('twi/', TwiWordView.as_view(), name='twi'),
]