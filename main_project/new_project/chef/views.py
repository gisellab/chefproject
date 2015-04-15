from django.shortcuts import render, redirect
from .forms import NewUserRestaurantForm, NewUserWorkerForm, NewUserProfileForm, NewRestaurantProfileForm
from chef.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from chef.models import PostNewJob
from django.utils.dateparse import parse_date

def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
                  'chef/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/chef/')


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
        # because the request.POST.get('<variable>') returns None, if the value does not exist,
        # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/userprofilepage/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your chef account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'chef/login.html', {})


def new_restaurant_user(request):
    if request.method == 'POST':
        form = NewUserRestaurantForm
        if form.is_valid():
            form.save()
    else:
        form = NewUserRestaurantForm
    context_dict = {'form': form}
    return render(request, 'new_restaurant_user.html', context_dict)


def new_worker_user(request):
    if request.method == 'POST':
        form = NewUserWorkerForm
        if form.is_valid():
            form.save()
    else:
        form = NewUserWorkerForm
    context_dict = {'form': form}
    return render(request, 'new_worker_user.html', context_dict)


def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'mainpage.html', context_dict)


def contact_us(request):
    return render(request, "contact_us.html")


def about(request):
    return HttpResponse("<br/> <a href='/about'>About</a>Guest Chef say this is the about page")


def mainpage(request):
    return render(request, 'mainpage.html')

def add_a_new_job(request):
    if request.POST:
        rawdate=request.POST['job_date']
        print rawdate
        parts=rawdate.split('/')
        cooked=[parts[2], parts[0], parts[1]]
        cooked="-".join(cooked)
        print cooked
        d=parse_date(cooked)
        print d
        job=PostNewJob()
        job.name_of_job=request.POST['job_name']
        job.restaurant_name=request.POST['restaurant_name']
        job.contact_name=request.POST['contact_name']
        job.date= d
        job.number_of_hours=int(request.POST['number_of_hours'])
        job.pay=int(request.POST['pay'])
        job.start_time=int(request.POST['start_time'])
        job.job_description=request.POST['job_description']
        job.poster=request.user
        job.save()
        redirect('jobs_pending')
    return render(request, 'add_a_new_job.html')

def buy_credit(request):
    return render(request, 'buy_credit.html')

def jobs_pending(request):
    return render(request, 'jobs_pending.html')

def previous_jobs(request):
    return render(request, 'previous_jobs.html')

def buy_credit_user(request):
    return render(request, 'buy_credit_user.html')

def jobs_pending_user(request):
    return render(request, 'jobs_pending_user.html')

def apply_for_a_new_job(request):
    return render(request, 'apply_for_a_new_job.html')

def previous_jobs_user(request):
    return render (request, 'previous_jobs_user.html')

def jobs_board(request):
    jobs=PostNewJob.objects.all()
    return render(request, 'jobs_board.html', {'jobs':jobs})


def edit_settings_restaurant(request):
    if request.method == 'POST':
        form = NewUserProfileForm
        if form.is_valid():
            form.save()

    else:
        form = NewUserProfileForm
        context_dict = {'form': form}
    return render(request, 'edit_settings_restaurant.html', context_dict)


def edit_settings_user(request):
    if request.method == 'POST':
        form = NewUserProfileForm
        if form.is_valid():
            form.save()
    else:
        form = NewUserProfileForm
    context_dict = {'form': form}
    return render(request, 'edit_settings_user.html', context_dict)


def facts_page(request):
    return render(request, 'facts_page.html')


def userprofilepage(request):
    # if request.method == 'POST':
    #     form = NewUserProfileForm
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = NewUserProfileForm
    # context_dict = {'form': form}
    return render(request, 'userprofilepage.html')


def restaurantprofilepage(request):
    if request.method == 'POST':
        form = NewRestaurantProfileForm
        if form.is_valid():
            form.save()
    else:
        form = NewRestaurantProfileForm
    context_dict = {'form': form}
    return render(request, 'restaurantprofilepage.html', context_dict)
