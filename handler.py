import json
import boto3
from datetime import datetime
import dateutil.tz
import random

session = boto3.session.Session()
ses = session.client('ses')

india = dateutil.tz.gettz('Asia/Kolkata')
IN_time = datetime.now(india)
current_time = IN_time.strftime("%H:%M %p")

water_quotes=[
    "Thousands Have Lived Without Love, Not One Without Water.",
    "No Water. No Life. No Blue. No Green.",
    "Water is Life. Don’t Waste It.",
    "Keep Calm & Drink Water.",
    "Water is Your Best Friend for Life.",
    "Pure Water is the World’s First and Foremost Medicine.",
    "Make Water Your Primary Drink instead of Soda, Juice. Choose Pure Water Throughout Your Day.",
    "Water is the Best Natural Remedy. Drink Your Way to Better Health.",
    "Water is Life and Clean Water is Means Health.",
    "Water is the Driving Force of All Nature.",
    "THINK, You Can’t do anything without water. Save it.",
    "Life starts with water"
]

quote_for_the_email = random.choice(water_quotes)

sender_email = 'jatinjmehrotra@gmail.com'
reciever_email = 'jain.cse2016.c@gmail.com'
#email_cc = 'Email' #optional
email_subject = 'Water reminder '
email_body =quote_for_the_email +  "\n\n" +'It\'s ' + current_time + ', time to drink water, Stay Hydrated!!!'

#print(email_body)


# def lambda_handler(event, context):


def lambda_handler(event, context):
    # TODO implement
    response = ses.send_email(
        Source = sender_email,
        Destination={
            'ToAddresses': [
                reciever_email,
            ]
            # 'CcAddresses': [   #optional
            #     email_cc,
            # ]
        },
        Message={
            'Subject': {
                'Data': email_subject
            },
            'Body': {
                'Text': {
                    'Data': email_body
                }
            }
        }
    )