import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image


##APP
def grayscale_filter(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def brightness_filter(img,level):
    img_ = cv2.convertScaleAbs(img, beta=level)
    return img_

def style_filter(img,sigma_s=60, sigma_r=0.07):
    img =cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.stylization(img, sigma_s=sigma_s, sigma_r=sigma_r)
    return img


def hdr_filter(img,sigma_s,sigma_r):
    img = cv2.convertScaleAbs(img,beta=0)
    img = cv2.detailEnhance(img, sigma_s=sigma_s, sigma_r=sigma_r)
    return img

def vintage_filter(img,level):
    hieght , width = img.shape[:2]
    x_kerenal = cv2.getGaussianKernel(width,width/level)
    y_kerenal = cv2.getGaussianKernel(hieght,hieght/level)
    kerenal = x_kerenal.T * y_kerenal
    mask = kerenal / kerenal.max()
    img_cpoy = np.copy(img)
    # img*kerenal
    for i in range(3):
        img_cpoy[:,:,i] = img_cpoy[:,:,i]*mask
        
    return img_cpoy

## GUI-------
st.title('Fliters APP')
st.write('Upload an image and apply various filters to it.')   

uploaded_image = st.file_uploader("upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    img = Image.open(uploaded_image)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    original , filtered =st.columns(2)
    
    with original:
        st.header("Original Image")
        st.image(img,channels= 'BGR')



    options = st.selectbox("Select a filter", 
                        ["None", "Grayscale", "Brightness", "Style", "HDR", "Vintage"])


    output_flag = 1
    color = 'BGR'

    if options == "None":
        output_flag = 0
        output_img = img
        
    elif options == "Grayscale":
        output_img=grayscale_filter(img)
        color = 'GRAY'

    elif options == "Brightness":
        level = st.slider("Brightness level", 0, 100,20)
        output_img=brightness_filter(img,level)

    elif options == "Style":
        sigma_s = st.slider("Sigma S", 0, 200,60)
        sigma_r = st.slider("Sigma R", 0.01, 1.0,0.07)
        output_img=style_filter(img,sigma_s,sigma_r)

    elif options == "HDR":
        sigma_s = st.slider("Sigma S", 0, 200,150)
        sigma_r = st.slider("Sigma R", 0.01, 1.0,0.25)
        output_img=hdr_filter(img,sigma_s,sigma_r)

    elif options == "Vintage":
        level = st.slider("Level", 0.0, 5.0,2.0,step=1.0)
        output_img=vintage_filter(img,level)
    
    
    
    with filtered:
        st.header("Filtered Image")
        st.image(output_img,channels= color)