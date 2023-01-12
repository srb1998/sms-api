import csv
import pytz
import os
import smtplib
import requests
from datetime import datetime
from dotenv import load_dotenv,find_dotenv
from fastapi import FastAPI

#To load .env file from the project folder
load_dotenv(find_dotenv())

#Initializing FastAPI
app = FastAPI()

#Checking conditions to send messages
def send_text_api(message:str,phone_number:str,country:str,api_key:str):
    
    if not 1<len(message)<=160:
        return "Invalid Message Length"

    if not isinstance(phone_number,int) or len(str(phone_number))==10:
        return "Invalid Phone Number"

    timezone = pytz.timezone(country)
    current_time = datetime.now(timezone)
    if not (current_time.hour>=10) and (current_time.hour<=17):
        return "Currently message cannot be sent. Try again between 10:00-5:00"

    base_url = "https://api.sms-magic.com/v1/sms/send"
    payload = f"mobile_number={phone_number}&sms_text={message}&sender_id=market"
    headers = {
      'apiKey': api_key,
      'content-type': "application/json",
      }
    response = requests.post(base_url, data=payload, headers=headers)
    if response.status_code==200:
        return "Success"
    else:
        return "Failed"

# Function to send email using python built in library smtplib
def send_email(to,message):

  sender_email = "sourabh@gmail.com"
  sender_password = "Your Password"

  msg = f"Subject:{message}"

  with smtplib.SMTP_SSL("xyz@gmail.com",465) as server:
    server.login(sender_email,sender_password)
    server.sendmail(sender_email,to,msg)
    print(f"Email send to {to}")


#Function for converting output into text file
def output_file(status, reason=None):
  with open("status.txt", "w") as f:
    if status == "success":
      return f.write("Success")
    elif status == "failure":
      if reason:
        return f.write("Failure: " + reason)
      else:
        return f.write("Failure")

#Home Page API 
@app.get("/")
def homepage():
  return "Please use http://127.0.0.1:8000/docs to open swagger homepage and easily navigate API's"

#Send text message API 
@app.post("/sendtext")
def text():
    api_key = os.getenv("API_KEY")
    with open('sample.csv','r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        message = row[0]
        email = row[1]
        phone = row[2]
        country = row[3]
        response = send_text_api(message,phone,api_key)
        if response=="Success":
            return output_file("success")
        else:
            return output_file("failure")

# Send mail API
@app.post("/sendemail")
def email():
    with open('sample.csv','r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        message = row[0]
        email = row[1]
        response = send_email(email,message)
    return "Email send succesfully"
