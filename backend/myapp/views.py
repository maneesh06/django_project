from logging import captureWarnings
from urllib import response
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
import json
from django.forms import BaseModelFormSet
from rest_framework.response import Response
from rest_framework import status
import datetime
from myapp.models import Person,PersonVisit,Unknown
from rest_framework.decorators import api_view
from myapp.seralizers import PersonSeralizer,PersonVisitSeralizer,UnknownVisitSeralizer
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

class BaseAuthorFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Person.objects.all()




@api_view(['GET','POST'])
def user_list(request):
    # to call get method response = requests.get("http://127.0.0.1:8000/user")
    if(request.method == 'GET'):
        user = Person.objects.all()
        seralizer = PersonSeralizer(user,many=True)
        return Response(seralizer.data)
    # to call post metnod requests.post("http://127.0.0.1:8000/user",{'first_name':'ajeet1','last_name':'yadav1'})
    elif request.method == 'POST':
        data = request.data
        person,createdy = Person.objects.get_or_create(
            first_name = data["first_name"],
            last_name = data["last_name"],
            roll_no = data["roll_no"],
            image = data["image"],
        )
        # captured_onn=datetime.datetime.now()
        PersonVisit.objects.create(person=person,captured_onn=datetime.datetime.now())
        data = json.dumps(data)
        # print(PersonVisit.objects.filter(person=person))
        return Response(data,status=status.HTTP_201_CREATED)
        
@api_view(['PUT','GET','DELETE'])
def user_detail(request,pk):
    try:
        user = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
    if(request.method == 'GET'):
        seralizer = PersonSeralizer(user)
        qs = PersonVisit.objects.all()
        qs = qs.filter(person_id = user.pk)
        l = []
        for query in qs:
            vser = PersonVisitSeralizer(query)
            l.append(vser.data)
        return Response(l)
    elif request.method == 'PUT':
        seralizer = PersonSeralizer(user,data = request.data)
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
