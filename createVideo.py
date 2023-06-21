import os
import cv2

path = "images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        images.append(file_name)
        
        
    count = len(images) 

frame = cv2.imread(images[0])
height,width,channel=frame.shape
size =(width,height)
print(size)

out = cv2.VideoWriter('Project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.5,size)

for i in range(0, count-1):
    frame = cv2.imread(images[i])
    out.write(frame)

print("done")