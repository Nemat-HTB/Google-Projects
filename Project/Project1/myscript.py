#! /usr/bin/env python3
from PIL import Image
import os
import shutil
import imghdr

#directory is where the images reside 
#change student-01-165ffc0ad351 by your username
directory = '/home/student-01-165ffc0ad351/images'
newdirectory ='/opt/icons/'


#First itrate through to'/home/student-01-165ffc0ad351/images' directory
for filename in os.listdir(directory):
        print(filename)
        print(imghdr.what(filename)) #this to know the file extention
        if imghdr.what(filename) == "tiff":

            im = Image.open('{}'.format(filename))
            im.rotate(90).resize((128,128)).convert('RGB').save(filename,'JPEG')
            print("Yasssssssss Converted")

            try :
                 #Now move image to '/opt/icons/' directory
                 dest = shutil.move(filename, newdirectory)
            except OSError:
                 continue


print("oooooooooo Finshed   ooooooooooooo")
