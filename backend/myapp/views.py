from django.shortcuts import render, HttpResponse
from django.http.response import StreamingHttpResponse
from myapp.camera import VideoCamera, IPWebCam

# Create your views here.
def index(request):
    # return HttpResponse("welcome to home page")
    contest = {
        "var" : 2555525
    }
    return render(request,"index.html",contest)

def about_us(request):
    return render(request,"about_us.html")

def contact_us(request):
    return render(request,"contact_us.html")

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
