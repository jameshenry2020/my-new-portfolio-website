from django.urls import path
from .views import HomePage, ProjectDetail, processing_contact



urlpatterns=[
    path('', HomePage.as_view(),name='home'),
    path('project-detail/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('contact/', processing_contact, name='contact')
]