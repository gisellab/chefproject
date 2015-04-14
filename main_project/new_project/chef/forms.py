from .models import UserRestaurant, UserWorker, NewUserProfile, NewRestaurantProfile, Skill, PostNewJob, UserProfile
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.models import User
from chef.models import Category, Page, UserProfile

# from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class NewUserRestaurantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewUserRestaurantForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout('auth_user', 'first_name', 'last_name', 'restaurant_name', 'email', 'tel_number',
                                    'address', 'times_hired', )
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    restaurant_name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    tel_number = forms.CharField(max_length=20)
    address = forms.CharField(max_length=255)
    times_hired = forms.IntegerField()

    class Meta:
        model = UserRestaurant


class NewUserWorkerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewUserWorkerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout('auth_user', 'first_name', 'last_name', 'email', 'tel_number', 'address',
                                    'times_hired', )
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    tel_number = forms.CharField(max_length=20)
    address = forms.CharField(max_length=255)
    times_hired = forms.IntegerField()

    class Meta:
        model = UserWorker


class NewUserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewUserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout('Name', 'Job_Description', 'Restaurants_worked', 'Job_titles_held',
                                    'Year_in_restaurant_industry', 'About_me', 'Upload_profile_picture', 'skill')
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    Name = forms.CharField(max_length=255)
    Job_Description = forms.CharField(max_length=255)
    Restaurants_worked = forms.CharField(max_length=255)
    Job_titles_held = forms.CharField(max_length=20)
    Years_in_restaurant_industry = forms.IntegerField()
    About_me = forms.CharField(widget=forms.Textarea, max_length=255)
    Upload_profile_picture = forms.ImageField()
    skill = forms.ModelMultipleChoiceField(Skill.objects.all())

    class Meta:
        model = NewUserProfile


class NewRestaurantProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewRestaurantProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout('Name_Restaurant', 'Restaurant_Description', 'Food_style', 'Main_contact_name',
                                    'About_the_restaurant', 'Signature_dish')
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    Name_Restaurant = forms.CharField(max_length=255)
    Restaurant_Description = forms.Textarea()
    Food_style = forms.Textarea()
    Main_contact_name = forms.CharField(max_length=255)
    About_the_restaurant = forms.Textarea()
    Signature_dish = forms.CharField(max_length=255)


    class Meta:
        model = NewRestaurantProfile


class PostNewJobForm(forms.ModelForm):
    name_of_job = forms.CharField(max_length=255)
    # User_type_required = forms.ForeignKey(UserType)
    date = forms.DateTimeField('measure date')
    pay = forms.IntegerField()
    number_of_hours = forms.IntegerField()

    def __unicode__(self):
        return self.name_of_job

    class Meta:
        model = PostNewJob



