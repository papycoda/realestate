from django.urls import path
from .views import ListingListView, ListingDetailView, SearchListings

urlpatterns = [
    path('', ListingListView.as_view(), name='listings'),\
    path('<slug>', ListingDetailView.as_view(), name='listing-detail'),
    path('search', SearchListings.as_view(), name='search-listings'),
]
