from django.urls import path
from .views import *

urlpatterns = [
    path('', RealtorListView.as_view()),
    path('mvp', MvpRealtorListView.as_view()),
    path('<int:pk>/', RealtorDetailView.as_view()),
]
