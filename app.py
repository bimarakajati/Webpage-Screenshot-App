import streamlit as st
import datetime, marshal, types
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse

# Load the code object from the .marshal file
with open('Functions/is_valid_url.marshal', 'rb') as file:
    is_valid_url_object = marshal.load(file)
with open('Functions/ss_web.marshal', 'rb') as file:
    ss_web_object = marshal.load(file)

# Create a new function from the loaded code object
is_valid_url = types.FunctionType(is_valid_url_object, globals())
ss_web = types.FunctionType(ss_web_object, globals())

st.sidebar.write("**Webpage Screenshot App**")

url_input = st.sidebar.text_input("Web URL:", key="url")
capture_button = st.sidebar.button("Take Screenshot")

if capture_button or url_input:
    if is_valid_url(url_input):
        with st.spinner("Taking screenshot... Please wait."):
            screenshot_filename = ss_web(url_input) # Capture the screenshot

        # Display the screenshot
        st.success("Screenshot taken successfully!")
        st.image(screenshot_filename)

        # Download the file
        st.download_button(label="Download Screenshot", data=open(screenshot_filename, 'rb'), mime='image/png')
    else:
        st.error("Please enter a full URL (including the scheme).")
else:
    st.info("Enter a URL and click on the button to capture a screenshot.")