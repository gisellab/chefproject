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


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Skill(models.Model):
    Chef = models.CharField(max_length=255)
    Server = models.CharField(max_length=255)
    Dishwasher = models.CharField(max_length=255)
    Bartender = models.CharField(max_length=255)

    def __str__(self):
        return self.Chef


class UserRestaurant(models.Model):
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
    name = models.CharField(max_length=255)
    Job_Description = models.CharField(max_length=255)
    Restaurants_worked = models.CharField(max_length=255)
    Job_titles_held = models.CharField(max_length=20)
    Years_in_restaurant_industry = models.IntegerField()
    About_me = models.TextField(max_length=150)
    Upload_profile_picture = models.ImageField(blank=True, null=True)
    skill = models.ManyToManyField(Skill)

    def __unicode__(self):
        return self.name


class NewRestaurantProfile(models.Model):
    Name_Restaurant = models.CharField(max_length=255)
    Restaurant_Description = models.TextField()
    Food_style = models.TextField()
    Main_contact_name = models.CharField(max_length=255)
    About_the_restaurant = models.TextField()
    Signature_dish = models.CharField(max_length=255)

    def __unicode__(self):
        return self.restaurant_name


class UserType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# class JobPoster(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __unicode__(self):
#         return self.name


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

    def __unicode__(self):
        return self.name_of_job


class ApplyForJob(models.Model):
    job = models.ForeignKey(PostNewJob)
    applicant = models.ForeignKey(User)
    date_applied = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.new_job_posting


class Message(models.Model):
    subject = models.CharField(max_length=150)
    body = models.CharField(max_length=300)
    from_user = models.ForeignKey(User)
    to_user = models.ForeignKey(User,null=True, related_name='+')
    job = models.ForeignKey(PostNewJob)

    def __unicode__(self):
        return self.subject



# class UserMessage(models.Model):
#     subject = models.CharField(max_length=150)
#     body = models.CharField(max_length=300)
#     user = models.ForeignKey(User)
#     job = models.ForeignKey(JobPoster)
#
#     def __unicode__(self):
#         return self.user






















