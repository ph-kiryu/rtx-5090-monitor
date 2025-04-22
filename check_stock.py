import requests
from bs4 import BeautifulSoup
import pushbullet
import telegram_notify

def check_stock():
    url = "https://marketplace.nvidia.com/de-de/consumer/graphics-cards/?locale=de-de&page=1&limit=12&gpu=RTX%205090&manufacturer=NVIDIA"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check for any product card not showing "Nicht auf Lager"
    in_stock = False
    for card in soup.find_all("div", class_="product-tile"):
        if "Nicht auf Lager" not in card.text:
            in_stock = True
            break

    if in_stock:
        message = "🚨 RTX 5090 FE might be in stock: " + url
        pushbullet.send_notification(message)
        telegram_notify.send_telegram(message)
    else:
        print("No stock found.")

if __name__ == "__main__":
    check_stock()
