from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from . models import Realtor
from . serializers import RealtorSerializer

class RealtorListView(ListAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

class RealtorDetailView(RetrieveAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    #lookup_field = 'id'

class MvpRealtorListView(ListAPIView):
    queryset = Realtor.objects.filter(is_mvp=True)
    serializer_class = RealtorSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None