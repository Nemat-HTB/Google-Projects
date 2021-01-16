#! /usr/bin/env python3

import os
import sys
import requests
import json

#Variables defintion
filedata = {'title':' ', 'name':' ', 'date': ' ','feedback': ' '} #Dictionary to store url prameter

for filename in os.listdir('/data/feedback'): #To itrerate through /data/feedback direcctory's file
s
    if filename.endswith(".txt") : #Just to check if file is text file

        file = open(os.path.join('/data/feedback',filename)).readlines() #open text file
        #print(file)
        

        filedata['title'] = file[0].rstrip("\n")
        filedata['name'] = file[1].rstrip("\n")
        filedata['date'] = file[2].rstrip("\n")
        line =""
        for lines in file[3:]:
            line = line + lines.rstrip()
        filedata['feedback']= line


        print ("feeeeeeeeeeeeeeeeeeld",filedata)
        #data1=json.dumps([{'title': k, 'name': v, 'date':d,'feedback':f } for k,v,d,f  in filedata.items()], indent=4)
        response = requests.post(r'http://35.184.142.153/feedback/', json=filedata) #change the IP 
        #print(data1)
        print(response.request.body)
        if not response.ok:
             raise Exception("GET failed with status code {}".format(response.status_code))

        continue
    else:
        continue

