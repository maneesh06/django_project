from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("welcome to home page")
    contest = {
        "var" : 2555525
    }
    return render(request,"index.html",contest
    )

def about_us(request):
    return render(request,"about_us.html")

def contact_us(request):
    return render(request,"contact_us.html")
