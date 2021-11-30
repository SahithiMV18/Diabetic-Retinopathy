# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import os
import shutil
print("hello")
#We should change the below path to the location where train.csv file is downloaded from Kaggle
df = pd.read_csv (r'C:\Users\Sahithi\Desktop\APTOS\train.csv')

for i, j in df.iterrows(): 
    diagnosiss = j
    i=0
    imageid = diagnosiss[0]
    print(imageid)
    diagnosis = diagnosiss[1]
    print(diagnosis)
    substring = "."
    substring1 = "+"
    if(imageid != "" and imageid.find(substring) != 1 and imageid.find(substring1) != 1):
        print(imageid)
        i=i+1
        print(i)
        #We should change below source path to location where we downloaded 3662 images from Kaggle
        sourcepath = r"C:\Users\Sahithi\Desktop\APTOS\traindummy"
        imagepath = imageid + ".png"
        source = os.path.join(sourcepath, imagepath)
        #we should change below destination path to the file location where we have precreated subfolders with labels 0,1,2,3,4
        destinationpath = r"C:\Users\Sahithi\Desktop\APTOS\dummy"
        destinationpath = os.path.join(destinationpath , str(diagnosis))
        print("SOURCE "+source)
        dest = shutil.move(source, destinationpath) 
    else:
        print('Exponential Value in csv:'+str(imageid))
        
        
