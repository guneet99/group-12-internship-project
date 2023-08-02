#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.models import load_model
from keras.preprocessing import image
import numpy
import cv2
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import re, csv, sys
model=load_model("C:/Users/hp/Desktop/xx/food.h5")


# In[2]:


def train_calorie_model(data_file):
    train = pd.read_csv(data_file)
    vectorizer = TfidfVectorizer(min_df=1, ngram_range=(1, 10))
    X_train = vectorizer.fit_transform(np.array(train.Food))
    model = MultinomialNB().fit(X_train, np.array(train.Calories))
    return model, vectorizer

def get_calorie(text):
    data_file = 'C:/Users/hp/Desktop/xx/calorie_dataset.csv'
    model, vectorizer = train_calorie_model(data_file)
    test = vectorizer.transform([text])
    return model.predict(test)

def createDict(calorie_file):
    calorie = pd.read_csv(calorie_file)
    d = {}
    i = 0
    for foodsubcategory in calorie.FoodSubcategory:
        d[foodsubcategory.lower()] = calorie.Calories[i]
        i = i + 1
    return d




# In[3]:


def prediction(path):
    img=image.load_img(path,target_size=(64,64))
    x=image.img_to_array(img)
    x=numpy.expand_dims(x,axis=0)
    pred=model.predict_classes(x)
    if(pred[0]==0):
        food ="burger"
    elif(pred[0]==1):
        food ="fries"
    elif(pred[0]==2):
        food = "pizza"
    else:
        food ="samosa"
    print(food)
    f = food
    d = createDict(calorie_file='C:/Users/hp/Desktop/xx/calorie_dataset.csv')
    print (food,"has %s calories." % get_calorie(food.lower()))
    
        
prediction('https://en.wikipedia.org/wiki/Pizza#/media/File:Eq_it-na_pizza-margherita_sep2005_sml.jpg')    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




