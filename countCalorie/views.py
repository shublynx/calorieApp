from django.shortcuts import render, redirect
from .models import Food, Consume
from django.contrib.auth import login,logout,authenticate,get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny




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
        username = request.POST['username']
        password = request.POST['password']
        user = get_user_model()
        # Create new user
        user = user.objects.create_user(username=username, password=password)

        # Authenticate and login the user
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('/')
    return render(request, 'auth/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

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










