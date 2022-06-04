
from rest_framework.response import Response
from rest_framework import status

from myapp.models import Unknown
from rest_framework.decorators import api_view
from myapp.seralizers import UnknownVisitSeralizer



@api_view(['GET','POST'])
def unknown_list(request):
    # to call get method response = requests.get("http://127.0.0.1:8000/user")
    if(request.method == 'GET'):
        user = Unknown.objects.all()
        seralizer = UnknownVisitSeralizer(user,many=True)
        return Response(seralizer.data)
    # to call post metnod requests.post("http://127.0.0.1:8000/user",{'first_name':'ajeet1','last_name':'yadav1'})
    elif request.method == 'POST':
        data = request.data
        person,createdy = Unknown.objects.create(
            image = data["image"],
        )
       
        return Response(status=status.HTTP_201_CREATED)
