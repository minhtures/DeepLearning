import streamlit as st
import os
import librosa
import numpy as np
from PIL import Image, ImageOps
from model import test,extract_feature
import soundfile
import torchvision
import sklearn
import torch
topic = {0:'Đời sống', 1:'Du lịch', 2:'Giải trí', 3:'Giáo dục', 4:'Khoa học', 5:'Kinh doanh',
6:'Pháp luật', 7:'Sức khỏe', 8:'Thế giới', 9:'Thể thao', 10:'Thời sự', 11:'Xe'}
st.sidebar.title("""
    Phân loại văn bản theo topic
""")
st.sidebar.subheader("App demo phân loại đơn giản")
_file = st.sidebar.file_uploader(
    "Please upload style txt file", type="txt")
option = st.sidebar.selectbox(
    'Lựa chọn mô hình để dự đoán',
    ('TF-IDF', 'Word2Vec', 'PhoBERT'))
if _file is None:
    st.sidebar.text("Bạn cần upload file text")

if st.sidebar.button('Phân loại'):
    if option == 'TF-IDF':
        mode = 1
        x = extract_feature(_file)
        st.markdown('Văn bản dược phân loại thuộc topic: **{}**.'.format(topic[test(x,mode)]))
    elif option == 'Word2Vec':
        mode = 2
        st.markdown('Văn bản dược phân loại thuộc topic: **{}**.'.format(topic[test(_file,mode)]))
    # else:
    #     mode = 3
#    try:
#    emotion=test(x,mode)
#    st.markdown('Văn bản dược phân loại thuộc topic: **{}**.'.format(test(x,mode)))