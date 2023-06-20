from django.shortcuts import render,redirect
from .models import Food,Consume


def index(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consumed = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consumed)
        consume.save()
        foods = Food.objects.all()


    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'countCalorie/index.html', {'food_items': foods, 'consumed_food': consumed_food})


def delete(request):
    pass

