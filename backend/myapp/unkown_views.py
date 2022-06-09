import os
from rest_framework.response import Response
from rest_framework import status
import base64
from myapp.models import Unknown
from rest_framework.decorators import api_view
from myapp.seralizers import UnknownVisitSeralizer
from PIL import Image
import io
import cv2
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
        # convert bytes data to PIL Image object
        img = Image.open(io.BytesIO(img_bytes))
        # img_arr = np.asarray(img)    
        print('*'*25, Path.cwd())
        # print(img_bytes,"/"*25)
        # img.show()
        base_dir = Path.cwd()
        image_file = os.path.join(base_dir,'media/unknown/22/monu.jpg')
        img.save(image_file)
        # image_file = 'media/photos/22/prashant.jpg'
        
        # with open(image_file, "rb") as f:
        #     im_bytes = f.read()
        # img = cv2.imread(image_file)
        Unknown.objects.create(
            image ="unknown/22/monu.jpg",
    
        )
        # print(data["image"],"*"*11)
       
        return Response(status=status.HTTP_201_CREATED)
