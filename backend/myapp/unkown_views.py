import os
from rest_framework.response import Response
from rest_framework import status
import base64
from myapp.models import Unknown
from rest_framework.decorators import api_view
from myapp.seralizers import UnknownVisitSeralizer
from PIL import Image
import io
import datetime
import numpy as np
from pathlib import Path


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
        im_b64 = data["image"]
        img_bytes = base64.b64decode(im_b64.encode('utf-8'))

        img = Image.open(io.BytesIO(img_bytes))

        base_dir = Path.cwd()
        captured_onn=datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

        image_file = os.path.join(base_dir,f'media/unknown/22/{captured_onn}')
        print(image_file)
        img.save(f'{image_file}.jpg')
        Unknown.objects.create(
            image = f"unknown/22/{captured_onn}.jpg",
    
        )
        return Response(status=status.HTTP_201_CREATED)
