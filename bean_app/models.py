from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from bean_app.google_maps_api import Mapper

'''
    *** NOTES: ***
    - Remember to add new models to bean_app/admin.py
    and to make migrations after making any changes 
    to the models.
    - We may need to include slugs for some of the objects
'''

mapper = Mapper()


class TagType(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return "Tag Type: {} pk: {}".format(self.name, self.pk)


class Tag(models.Model):
    tag_type = models.ForeignKey(TagType, blank=True, default=None)
    value = models.IntegerField(default=0)
    coffee_bean = models.ForeignKey('CoffeeBean', default=None,
                                    blank=True, related_name='tags')

    def __str__(self):
        return "{}".format(self.tag_type.name)


class CoffeeBean(models.Model):
    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(blank=True)  # Just making this blank for testing
    location = models.CharField(max_length=128)  # This might need to be coordinates depending on the google maps api
    description = models.CharField(max_length=1000, blank=True)
    price = models.FloatField(default=None, blank=True, null=True)
    average_rating = models.FloatField(default=0)
    t_type = models.CharField(max_length=128,
                              blank=True)  # what is type exactly? Need different name/ clashes with python built in type
    # tags = models.ForeignKey(Tag, related_name='coffee_beans')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CoffeeBean, self).save(*args, **kwargs)

    class Meta:
        ordering = ('average_rating',)

    def __str__(self):
        return "Coffee bean: {} - {}".format(self.pk, self.name)

# THIS CLASS IS NO LONGER NEEDED

# class Customer(models.Model):
#     # We don't need a customer id number do? Just use to pk?
#     fullname = models.CharField(max_length=128)
#     email = models.EmailField()
#     # password = models.CharField()   This would store the password as a string, Django handles this for us
#     # address = models.CharField()      Do we need their address?
#     # telephone = models.CharField()   Do we need the telephone?
#     favourite_coffee = models.ForeignKey(CoffeeBean)
#
#     # Makes more sense to have the link here, rather than the char field?
#
#     def __str__(self):
#         return "Customer: {} - {}".format(self.pk, self.fullname)


# This class, combined with the standard user class will eventually replace the customer object above
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    saved_coffees = models.ManyToManyField(CoffeeBean)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    user = models.ForeignKey(User, blank=True, default=None)
    coffee_bean = models.ForeignKey(CoffeeBean)
    # Don't need to use '_id' in the variable name. ORM allows us to just treat this as the object rather than a pk
    rating = models.IntegerField()  # Why float field? I just assumed we would be using a star system or something?
    comment = models.TextField(max_length=240, blank=True)

    def __str__(self):
        return "Review: {} of {} by {}".format(self.pk, self.coffee_bean, self.customer)


class Vendor(models.Model):
    owner_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    business_name = models.CharField(max_length=128, unique=True)
    # password = models.CharField()
    url_online_shop = models.URLField(blank=True)
    address = models.CharField(max_length=128)
    # telephone = models.CharField()
    description = models.TextField(max_length=1000, blank=True)
    products_in_stock = models.ManyToManyField(CoffeeBean)
    # In order to display the vendor on the map we need to save the lat and long coordinates
    lat = models.FloatField(default=None, blank=True)
    long = models.FloatField(default=None, blank=True)

    # Before saving, take the address and get the formatted address
    # and the coordinates for the cafe
    def save(self, *args, **kwargs):
        data = mapper.geocode(address=self.address)
        self.address, self.lat, self.long = data
        super(Vendor, self).save(*args, **kwargs)


    # This could be useful, if we can implement it
    # def has_online_shop(self):
    #     return True if url_online_shop exits

    def __str__(self):
        return "Vendor: {} - {} - {}".format(self.pk, self.owner_name, self.business_name)


class AccountForm(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class VendorAccountForm(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class VendorSignupForm(models.Model):
    pass


class SignupForm(models.Model):
    pass
