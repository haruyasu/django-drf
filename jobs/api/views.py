from rest_framework import generics
from jobs.models import JobOffer
from jobs.api.permissions import IsAdminUserOrReadOnly
from jobs.api.serializers import JobOfferSerializer


class JobOfferListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobOffer.objects.all().order_by("-id")
    serializer_class = JobOfferSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class JobOfferDetailAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer
    permission_classes = [IsAdminUserOrReadOnly]
