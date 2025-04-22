import requests
from bs4 import BeautifulSoup
import pushbullet
import telegram_notify
import datetime

def log(message):
    print(f"[{datetime.datetime.now().isoformat()}] {message}")

def check_stock():
    url = "https://marketplace.nvidia.com/de-de/consumer/graphics-cards/?locale=de-de&page=1&limit=12&gpu=RTX%205090&manufacturer=NVIDIA"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    log("Requesting NVIDIA page...")
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        log(f"Failed to fetch page: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all("div", class_="product-tile")
    log(f"Found {len(cards)} product tiles.")

    in_stock = False
    for card in cards:
        if "Nicht auf Lager" not in card.text:
            log("🚨 Found a card that might be in stock!")
            in_stock = True
            break

    if in_stock:
        message = "🚨 RTX 5090 FE might be in stock: " + url
        log("Sending alerts...")
        pushbullet.send_notification(message)
        telegram_notify.send_telegram(message)
    else:
        log("No stock found.")

if __name__ == "__main__":
    check_stock()
