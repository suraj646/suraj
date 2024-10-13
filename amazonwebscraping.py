from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
URL='https://www.amazon.in/Steelbird-SBH-34-Jai-Shree-Ram/dp/B0CTK1R6L7/ref=s9_acsd_al_ot_c2_x_0_t?_encoding=UTF8&pf_rd_t='
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-66eecfc7-6e2793c35bf73a8b2e42bd54"}
page=requests.get(URL,headers=headers)
soup1=BeautifulSoup(page.content,"html.parser")
soup2=BeautifulSoup(soup1.prettify(),"html.parser")
title=soup2.find(id='productTitle').get_text();
price=soup2.find(class_='a-offscreen').get_text();
# title,price
# print(title),print(price)
price=price.strip()[1:]
title=title.strip()
print(title),print(price);
today=datetime.date.today()
print(today)
import csv
header=['Product_Name','Price','Date']
data=[title,price,today]
with open('AmazonWebScraper.csv','w',newline='',encoding='UTF8') as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
import pandas as pd
df=pd.read_csv(r"C:\Users\suraj\surajpanda\AmazonWebScraper.csv")
df
# now we are appending data
def check_price():
    URL='https://www.amazon.in/Steelbird-SBH-34-Jai-Shree-Ram/dp/B0CTK1R6L7/ref=s9_acsd_al_ot_c2_x_0_t?_encoding=UTF8&pf_rd_t='
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-66eecfc7-6e2793c35bf73a8b2e42bd54"}
    page=requests.get(URL,headers=headers)
    soup1=BeautifulSoup(page.content,"html.parser")
    soup2=BeautifulSoup(soup1.prettify(),"html.parser")
    title=soup2.find(id='productTitle').get_text()
    price=soup2.find(class_='a-offscreen').get_text()
    title=title.strip()
    price=price.strip()[1:]
    today=datetime.date.today()
    import csv
    header=['Product_Name','Price','Date']
    data=[title,price,today]
    with open('AmazonWebScraper.csv','a+',newline='',encoding='UTF8') as f:
        writer=csv.writer(f)
        writer.writerow(data)
    if price <1000:
        send_mail;
while (True):
    check_price()
    time.sleep(86400)
    
