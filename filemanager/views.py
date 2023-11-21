from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from .forms import *
from filemanager.models import *
from django.shortcuts import redirect
from django.contrib.auth import login
from .home import *

# Login view function
def login(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Create an authentication form with the provided POST data
        auth_form = AuthenticationForm(request=request, data=request.POST)
        print(auth_form.errors)
        # Check if the form is valid
        if auth_form.is_valid():
            # Retrieve username and password from the form data
            username = auth_form.cleaned_data.get("username")
            password = auth_form.cleaned_data.get("password")
            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            # Check if the user is authenticated
            if user is not None:
                # Store user ID in the session and redirect to the home page
                request.session['user'] = user.id
                return redirect('/home/1')
            else:
                # If authentication fails, redirect back to the login page
                return redirect('login')
        else:
            # If form is not valid, print an error message
            print('Authentication form is not valid')
    else:
        # If the request method is not POST, create an empty authentication form
        auth_form = AuthenticationForm()

    # Render the login.html template with the authentication form
    return render(request, "login.html", context={"form": auth_form})

# Register view function
def register(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Create a registration form with the provided POST data
        auth_form = RegisterAuthenticationForm(data=request.POST)
        print(auth_form.is_valid())
        # Check if the form is valid
        if auth_form.is_valid():
            # Retrieve username and password from the form data
            username = auth_form.cleaned_data.get("username")
            password = auth_form.cleaned_data.get("password1")
            print(auth_form.cleaned_data.keys())
            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            # Check if the user does not already exist
            if user is None:
                # Create a new user and redirect to the login page
                User.objects.create_user(username=username,
                                         password=password,
                                         first_name=auth_form.cleaned_data.get("first_name"),
                                         last_name=auth_form.cleaned_data.get("last_name")
                                         )
                return redirect('login')

    else:
        # If the request method is not POST, create an empty registration form
        auth_form = RegisterAuthenticationForm()

    # Render the register.html template with the registration form
    return render(request, "register.html", context={"form": auth_form})
