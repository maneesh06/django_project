from urllib import response
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from matplotlib.font_manager import json_dump
from rest_framework.response import Response
from rest_framework import status
from myapp.models import UserData
import json
from rest_framework.decorators import api_view
from myapp.seralizers import UserDataSeralizer

# Create your views here.
def index(request):
    data = UserData.objects.all()
    # return HttpResponse("welcome to home page")
    contest = {
        "data" : list(data.values('first_name'))
    }
    print(contest["data"][0])
    # json_object = json.dumps(contest, indent = 4) 
    # print(json_object)
    return JsonResponse(contest)
    # return render(request,"home.html",contest)

def about_us(request):
    return render(request,"about_us.html")

def contact_us(request):
    return render(request,"contact_us.html")


@api_view(['GET','POST'])
def user_list(request):
    # to call get method response = requests.get("http://127.0.0.1:8000/user")
    if(request.method == 'GET'):
        user = UserData.objects.all()
        seralizer = UserDataSeralizer(user,many=True)
        return Response(seralizer.data)
    # to call post metnod requests.post("http://127.0.0.1:8000/user",{'first_name':'ajeet1','last_name':'yadav1'})
    elif request.method == 'POST':
        data = request.data
        user = UserData.objects.create(
            first_name = data["first_name"],
            last_name = data["last_name"]
        )
        data = json_dump(data)
        return Response(data,status=status.HTTP_201_CREATED)
        
            

        
        #     return Response(seralizer.data,status = status.HTTP_201_CREATED)
        # else:
        return Response(status=status.HTTP_200_OK)
@api_view(['PUT','GET','DELETE'])
def user_detail(request,pk):
    try:
        user = UserData.objects.get(pk=pk)
    except UserData.DoesNotExist:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
    if(request.method == 'GET'):
        seralizer = UserDataSeralizer(user)
        return Response(seralizer.data)
    elif request.method == 'PUT':
        seralizer = UserDataSeralizer(user,data = request.data)
        if seralizer.is_valid:
            seralizer.save()
            return Response(seralizer.data,status=status.HTTP_202_ACCEPTED)

        return Response(seralizer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

