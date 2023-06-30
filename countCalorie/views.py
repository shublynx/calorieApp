from django.shortcuts import render, redirect
from .models import Food, Consume
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from calorieApp import settings
from django.core.mail import send_mail


def index(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()


    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'countCalorie/index.html', {'foods': foods, 'consumed_food': consumed_food})



def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('login/index/')
    return redirect('/login/index')



def home(request):
    return render(request, 'auth/home.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username):
            messages.error(request,"Username is taken")

        if User.objects.filter(email=email):
            messages.error(request,"Email already registered")

        if len(username)>10 or username.isalnum():
            messages.error(request,"Username must be alphanumeric and under 10 characters")
        # Create new user
        user = User.objects.create_user(username=username, password=password, email=email)

        user.save()

        # Welcome mail

        subject = "Welcome"
        message = "Welcome"+ user.username +"!!!"
        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]
        send_mail(subject,message,from_email,to_email,fail_silently=True)



        return redirect('/')
    return render(request, 'auth/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate and login the user
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("index/")
        else:
            return render(request,'auth/login.html',{ 'error' : 'Invalid Credentials'})
    return render(request,'auth/login.html')


def user_logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect("/")










