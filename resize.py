import os
from PIL import Image

files = os.listdir("./images")

for i in range(len(files)):
    image = Image.open("./images/"+files[i])
    rimage = image.resize((50,50))
    rimage.save(files[i])
