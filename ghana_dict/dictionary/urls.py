from django.urls import path
from dictionary.views import *


urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('word/', WordView.as_view(), name='word'),
]