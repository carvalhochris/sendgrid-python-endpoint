import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = 'https://api.sendgrid.com/v3/mail/send'
api_key = os.getenv('SENDGRID_API_KEY')
email_address = os.getenv('TO_EMAIL_ADDRESS')

data = {
    'personalizations': [
        {
            'to': [
                {
                    'email': email_address,
                    'name': 'Recipient Name'
                }
            ],
            'subject': 'Hello there!'
        }
    ],
    'content': [
        {
            'type': 'text/plain',
            'value': 'Hello world!'
        }
    ],
    'from': {
        'email': 'chris@unlockyoursound.com',
        'name': 'Christopher'
    },
    'reply_to': {
        'email': 'chris@unlockyoursound.com',
        'name': 'Christopher'
    }
}

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 202:
    print('Email sent successfully')
else:
    print(f'Error sending email: {response.content}')
