from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Listing
from .serializers import ListingSerializer, ListingDetailSerializer
from datetime import datetime, timedelta,timezone

class ListingListView(ListAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ListingSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'


class ListingDetailView(RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer
    lookup_field = 'slug'

class SearchListings(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ListingDetailSerializer
    def post(self, request, format=None):
        queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
        data = request.data
        if 'home_type' in data:
            queryset = queryset.filter(home_type__iexact=data['home_type'])
        if 'city' in data:
            city = data['city']
            queryset = queryset.filter(city__iexact=city)
        if 'state' in data:
            state = data['state']
            queryset = queryset.filter(state__iexact=state)
        if 'bedrooms' in data:
            bedrooms = data['bedrooms']
            queryset = queryset.filter(bedrooms__iexact=bedrooms)
        if 'bathrooms' in data:
            bathrooms = data['bathrooms']
            queryset = queryset.filter(bathrooms__iexcact=bathrooms)
        #set a minimum price and only return listings that are greater than or equal to the minimum price
        if 'min_price' in data:
            min_price = data['min_price']
            queryset = queryset.filter(price__gte=min_price)
        #set a maximum price and only return listings that are less than or equal to the maximum price
        if 'max_price' in data:
            max_price = data['max_price']
            queryset = queryset.filter(price__lte=max_price)
        if 'sqft' in data:
            sqft = data['sqft']
            queryset = queryset.filter(sqft__gte=sqft)

        for query in queryset:
            days_ago = datetime.now(timezone.utc) - timedelta(days=30)
            if days_ago!=0:
                if query.list_date < days_ago:
                    queryset = queryset.exclude(slug__iexact=query.slug)


        serializer = ListingDetailSerializer(queryset, many=True)
        return Response(serializer.data)
