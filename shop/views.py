from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return HttpResponse("Hello, world! You'ra at the shop!")

def login(request):
    return HttpResponse("Logowanie")

def add_to_cart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            
            cartForm=CartForm({
                "user":request.user,
                "product_id":request.POST["product_id"],
                "quantity":request.POST["quantity"],
                "size":request.POST["size"]
            })

            temp={}
            for key, value in request.POST.items():
                temp[key]=value
            temp_json = json.dumps(temp,)
            print(temp_json)

            if cartForm.is_valid():
                print("valid")
                cartForm.save()
            else:
                error=json.dumps(cartForm.errors.as_json())
                print(error)
                return JsonResponse(error, status=400,safe=False)

            return JsonResponse(status=200,safe=False)
        else:
            return JsonResponse({"error": "not logged in"}, status=400,safe=False)

    print("error")
    return JsonResponse({"error": ""}, status=400,safe=False)

