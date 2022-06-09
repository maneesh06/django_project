
import requests
import os
import base64
from pathlib import Path
from pathlib import WindowsPath
import numpy
from PIL import Image
image_file = '1.jpg'
with open(image_file, "rb") as f:
    im_bytes = f.read()        
im_b64 = base64.b64encode(im_bytes).decode("utf8")
print(im_bytes)
# files = {'image': open('1.jpg')}
# print(files)
# response = requests.get("http://127.0.0.1:8000/user?page=1")
url ="http://127.0.0.1:8000/unknown"
# res = requests.post(url,{'image':files, 'first_name':'testing',"last_name":".","roll_no":1805231034})
res = requests.post(url,{'image':im_b64})
print(res)
