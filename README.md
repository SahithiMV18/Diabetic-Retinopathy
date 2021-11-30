# Diabetic-Retinopathy
Original Source link from Kaggle: https://www.kaggle.com/c/aptos2019-blindness-detection/data
From the above link we can download the dataset which we used in our project. We used train_images folder and train.csv file from this dataset. This train_images folder contains 3662 images with unique id. The train.csv file has the unique id column and diagnosis column.
The train_images folder should be filtered into five different categories where each category corresponds to one class. We have five different classes 0,1,2,3,4.
The file “/filterimagescode” in this folder which I have attached contains python code which we should run for filtering the images into five different category based on their diagnosis value read from train.csv file which is downloaded from Kaggle. This is mandatory step to do before running the models. The file paths which should be modified in the python code are mentioned in the form of  comments in the same python code file.
