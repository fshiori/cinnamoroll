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
    # 检查标准输入是否来自管道
    if sys.stdin.isatty():
        print("Error: Please provide input through a pipe", file=sys.stderr)
        sys.exit(1)
    
    # 从管道读取所有输入
    message = sys.stdin.read()
    
    if message:
        send_to_gchat(message)
    else:
        print("No message provided")
        sys.exit(1)
