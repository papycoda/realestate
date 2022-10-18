from matplotlib.pyplot import title
from rest_framework import serializers
from .models import Listing

#all listings serializer

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title', 'address', 'city','state', 'description', 'sale_type', 'home_type', 'price', 'bedrooms', 'bathrooms', 'garage_spaces', 'sqft', 'photo_main', 'list_date')

class ListingDetailSerializer  (serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        lookup_field = 'slug'
        