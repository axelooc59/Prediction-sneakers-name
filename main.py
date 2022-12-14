import streamlit as st
import os, sys





from PIL import Image
st.title("Sneakers prediction name")
st.markdown("##### Using reverse search google image engine")
st.write("find the code on my github [here](https://github.com/axelooc59/Prediction-sneakers-name)")

from selenium.webdriver.common.by import By
import requests

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options=webdriver.FirefoxOptions() 
options.add_argument("--lang=fr")
options.add_argument("--headless")

driver=webdriver.Firefox(options=options,executable_path="geckodriver.exe")


filename=st.file_uploader("Upload a picture",type=["png","jpg"])
if st.button('Find name'):
    if filename is not None:
        with st.spinner('Searching...'):
            

            image2 = Image.open(filename)
            image2.save("pic.png")
            st.image(image2,caption="Picture to predict")
            

            filePath = 'pic.png'
            searchUrl = 'http://www.google.hr/searchbyimage/upload'
            multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
            response = requests.post(searchUrl, files=multipart, allow_redirects=False)

            fetchUrl = response.headers['Location']
            print(fetchUrl)

            driver.get(fetchUrl)

            input=driver.find_element(By.TAG_NAME,"input")
            name=input.get_attribute("value")
            new_name=name +" site:stockx.com"
            print(new_name)
            driver.execute_script(f"document.getElementsByTagName('input')[0].setAttribute('value','{new_name}')") # add filter  site:stockx.com
            driver.find_element(By.ID,"L2AGLb").click()#click cookies
            driver.find_element(By.CLASS_NAME,"zgAlFc").click() #click search button 

            res=driver.find_element(By.TAG_NAME,"h3")
            res=res.text.split("-")[0]
        st.success(f"Name is : {res}")
    else:
         st.error("Please update a picture")
         
    


