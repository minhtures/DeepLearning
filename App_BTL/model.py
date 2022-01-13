import os
import soundfile
import librosa
import numpy as np
import pickle
import sklearn
from keras.models import  load_model
import w2vclassifier
def extract_feature(file_name):
    tf_idf=pickle.load(open('models/TFIDF.pkl', 'rb'))
    x=[]
    x.append(str(file_name.read(),"utf-8"))
    result = tf_idf.transform(x)
    return result
def extract_feature2(file_name):
    x=[]
    x.append(w2vclassifier.classify(str(file_name.read(),"utf-8")))
    return x[0]
def test(file_text, mode):
    topic=''
    if mode == 1:
        dnn=load_model("models/dnn.save")
        topic = dnn.predict(file_text)[0].argmax(axis=-1)
    if mode == 2:
        topic = extract_feature2(file_text)
    # elif mode == 2:
    #     w2v=pickle.load(open('models/rf_model', 'rb'))
    #     topic = rf.predict(file_text)[0]
    # else:
    #     mlp=pickle.load(open('models/mlp_model', 'rb'))
    #     topic = mlp.predict(file_text)[0]
    return topic