from urllib import response
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from matplotlib.font_manager import json_dump
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes,permission_classes

from myapp.models import UserData

from rest_framework.decorators import api_view
from myapp.seralizers import UserDataSeralizer
from django.http.response import StreamingHttpResponse
from myapp.camera import VideoCamera, IPWebCam

# Create your views here.
def index(request):
    return render(request,"index.html")

def prashant(request):
    return render(request,"home.html")

def about_us(request):
    return render(request,"about_us.html")

def contact_us(request):
    return render(request,"contact_us.html")


@api_view(['GET','POST'])
@authentication_classes([ BasicAuthentication])
@permission_classes([IsAuthenticated])
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

def live_streaming(request):
    return render(request,"live_streaming.html")

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')


def webcam_feed(request):
	return StreamingHttpResponse(gen(IPWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')
