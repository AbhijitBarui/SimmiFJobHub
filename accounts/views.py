from django.forms import model_to_dict
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth

def register(request):
    if request.method == "POST":
        #register user logic
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #password match check
        if password == password2:
            #check username:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is already taken')
                return redirect('register')
            else:
                #check email:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'that email is already registered with us')
                    return redirect('login')
                else:
                    #looks good
                    user = User.objects.create_user(
                        username =username,
                        password = password,
                        email = email,
                        first_name = first_name,
                        last_name = last_name,
                    )
                    #login after register:
                    auth.login(request, user)
                    messages.success(request, 'you are now logged in')
                    return redirect('index')
                    #manual login:
                    #user.save()
                    #messages.success(request, 'you are now registered, please proceed to log in)
                    #return redirect('login)
        else:
            messages.error(request, 'passwords do not match')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == "POST":
        #login suer logic
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')
        return
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'you are now logged out')
        return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        context = model_to_dict(request.user)
    return render(request, 'accounts/dashboard.html', context)

#context of user
# {'id': 1, 
# 'password': 'pbkdf2_sha256$320000$COYPRR9aaL47ReuWwyVPuN$1k5hnx9m1fHOaF985uGWpQGtNOVQqxRgxuUgg9uqqPs=', 
# 'last_login': datetime.datetime(2022, 5, 15, 19, 30, 2, 221333, tzinfo=datetime.timezone.utc),
#  'is_superuser': True, 'username': 'abhijit', 'first_name': '', 'last_name': '', 
# 'email': 'abhijitongit@gmail.com', 'is_staff': True, 'is_active': True,
#  'date_joined': datetime.datetime(2022, 5, 14, 19, 44, 36, 146629, tzinfo=datetime.timezone.utc), 
# 'groups': [], 'user_permissions': []}