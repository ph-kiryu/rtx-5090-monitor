import requests
import os

def send_notification(message):
    token = os.getenv("PUSHBULLET_TOKEN")
    if not token:
        print("Pushbullet token not found.")
        return

    data = {
        "type": "note",
        "title": "RTX 5090 FE Alert",
        "body": message
    }
    response = requests.post(
        "https://api.pushbullet.com/v2/pushes",
        json=data,
        headers={"Access-Token": token}
    )
    print("Pushbullet notification sent." if response.status_code == 200 else "Pushbullet error.")
