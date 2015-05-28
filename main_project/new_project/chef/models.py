from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.title


class UserType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Skill(models.Model):
    Chef = models.CharField(max_length=255)
    Server = models.CharField(max_length=255)
    Dishwasher = models.CharField(max_length=255)
    Bartender = models.CharField(max_length=255)

    def __str__(self):
        return self.Chef


class UserRestaurant(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    # auth_user = models.OnetoOneField(User, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    restaurant_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    tel_number = models.IntegerField(max_length=255)
    address = models.CharField(max_length=255)
    times_hired = models.IntegerField(default=0)

    def __unicode__(self):
        return self.email


class UserWorker(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    # auth_user = models.OnetoOneField(User, primary_key = True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    tel_number = models.IntegerField(max_length=255)
    address = models.CharField(max_length=255)
    times_hired = models.IntegerField(default=0)

    def __unicode__(self):
        return self.email


class NewUserProfile(models.Model):
    # auth_user = models.OnetoOneField(User, primary_key = True)
    type = models.ForeignKey(UserType, blank=True, null=True)
    profile = models.ForeignKey(User, related_name='profile')
    name = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    job_description = models.CharField(max_length=255, null=True, blank=True)
    previous_restaurants = models.CharField(max_length=255, null=True, blank=True )
    job_titles_held = models.CharField(max_length=20, null=True, blank=True)
    years = models.CharField(max_length=20, null=True, blank=True)
    about_me = models.TextField(max_length=150,null=True, blank=True )
    Upload_profile_picture = models.ImageField(blank=True, null=True)
    # skill = models.ManyToManyField(Skill)

    def __unicode__(self):
        return self.profile.username


class NewRestaurantProfile(models.Model):
    profile = models.ForeignKey(User, related_name='restaurant')
    type = models.ForeignKey(UserType, blank=True, null=True)
    Name_Restaurant = models.CharField(max_length=255,null=True, blank=True )
    restaurant_address = models.TextField(null=True, blank=True)
    Main_contact_name = models.CharField(max_length=255)
    contact_number = models.IntegerField(null=True, blank=True)
    contact_email = models.TextField(null=True, blank=True)
    food_style = models.TextField(null=True, blank=True)
    Signature_dish = models.CharField(max_length=255)

    def __unicode__(self):
        return self.profile.username


class PostNewJob(models.Model):
    name_of_job = models.CharField(max_length=100)
    restaurant_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_telephone = models.IntegerField()
    poster = models.ForeignKey(User)
    date_of_job = models.CharField(max_length=255)
    pay_per_hour = models.IntegerField()
    number_of_hours = models.IntegerField()
    start_time = models.IntegerField()
    description = models.CharField(max_length=150)
    type = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name_of_job


class Applicant(models.Model):
    job = models.ForeignKey(PostNewJob, related_name='applicant')
    applicant = models.ForeignKey(User)
    date_applied = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.new_job_posting


class Message(models.Model):
    subject = models.CharField(max_length=150)
    body = models.CharField(max_length=300)
    from_user = models.ForeignKey(User)
    to_user = models.ForeignKey(User, null=True, related_name='+')
    job = models.ForeignKey(PostNewJob)

    def __unicode__(self):
        return self.subject

























