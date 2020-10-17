#import yfinance as yf
#import streamlit as st
#import pandas as pd
#import matplotlib.pyplot as plt
#st.set_option('deprecation.showfileUploaderEncoding', False)

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

PATH="C:\Program Files (x86)\msedgedriver.exe"
driver=webdriver.Edge(PATH)
driver.get('https://www.fool.com/earnings/call-transcripts/2020/07/31/exxonmobil-xom-q2-2020-earnings-call-transcript.aspx')
words=driver.find_element_by_class_name('full_article').text

print(words)

driver.quit()
pd.DataFrame(x for x in (words.split('.')))
