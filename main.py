from PIL import Image

open

def formatImageData(imgData):
    imgArray = []
    for i in range(int(len(imgData)/4)):
        imgArray.append((imgData[i*4], imgData[(i*4)+1], imgData[(i*4)+2], imgData[(i*4)+3]))
    return imgArray

img = Image.open("./images/5.1.12.png","r")
imgData = list(img.getdata())

fImgData = formatImageData(imgData)

file = open("bigData2.txt","w")
file.write(str(fImgData).replace(")", ")\n").replace("[","").replace("]","").replace(", (", "(").replace(" ",""))



