from django.db import models
from django.utils.timezone import now
from realtors.models import Realtor

# Create your models here.\
class Listing(models.Model):
    class Saletype(models.TextChoices):
        Sale = 'Sale', 'For Sale'
        Rent = 'Rent', 'For Rent'
    class HomeType(models.TextChoices):
        House = 'House', 'House'
        Apartment = 'Apartment', 'Apartment'
        Condo = 'Condo', 'Condo'
        Townhouse = 'Townhouse', 'Townhouse'
        Land = 'Land', 'Land'
        Other = 'Other', 'Other'
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING,default=None)
    slug = models.CharField(max_length=200, unique=True)
    # Listing title
    title = models.CharField(max_length=200)
    # Listing address
    address = models.CharField(max_length=200)
    # Listing city
    city = models.CharField(max_length=100)
    # Listing state
    state = models.CharField(max_length=100)
    # Listing zip code
    zipcode = models.CharField(max_length=20)
    # Listing description
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=100, choices=Saletype.choices, default = Saletype.Sale)
    home_type = models.CharField(max_length=100, choices=HomeType.choices, default = HomeType.House)
    # Listing price
    price = models.IntegerField()
    # Listing bedrooms
    bedrooms = models.IntegerField()
    # Listing bathrooms
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    # Listing garage spaces
    garage_spaces = models.IntegerField(blank=True, null=True)
    # Listing sqft
    sqft = models.IntegerField()
    # Listing photo
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    # Listing photo 2
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # Listing photo 3
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # Listing photo 4
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # Listing photo 5
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # Listing photo 6
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # Listing is published
    is_published = models.BooleanField(default=True)
    # Listing list date
    list_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

