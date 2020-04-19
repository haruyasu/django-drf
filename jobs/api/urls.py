from django.urls import path
from jobs.api.views import (JobOfferListCreateAPIView, JobOfferDetailAPIview)

urlpatterns = [
    path("jobs/", JobOfferListCreateAPIView.as_view(), name="job-list"),
    path("jobs/<int:pk>/", JobOfferDetailAPIview.as_view(), name="job-detail"),
]
