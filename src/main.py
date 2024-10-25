import os
import sys
from dotenv import load_dotenv
import requests

load_dotenv()

def send_to_gchat(message):
    webhook_url = os.environ.get('GCHAT_WEBHOOK_URL')
    if not webhook_url:
        print("Error: GCHAT_WEBHOOK_URL environment variable is not set", file=sys.stderr)
        sys.exit(1)

    payload = {'text': message}
    response = requests.post(webhook_url, json=payload)
    
    if response.status_code == 200:
        print("Message successfully sent to Google Chat")
    else:
        print(f"Failed to send message, status code: {response.status_code}", file=sys.stderr)

if __name__ == "__main__":
    # Read all input from stdin
    message = sys.stdin.read()
    
    if message:
        send_to_gchat(message)
    else:
        print("Error: No message provided", file=sys.stderr)
        sys.exit(1)
