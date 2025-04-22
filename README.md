# RTX 5090 FE Stock Checker (GitHub Actions)

This GitHub Action monitors the NVIDIA Germany marketplace for RTX 5090 Founders Edition availability.

## How It Works

- Checks the product page every 10 minutes
- Sends alerts via:
  - Pushbullet
  - Telegram (optional)

## Setup

1. Fork or clone this repo
2. Add GitHub secrets:
   - `PUSHBULLET_TOKEN`
   - `TELEGRAM_TOKEN` (optional)
   - `TELEGRAM_CHAT_ID` (optional)
3. Enable Actions in your repo
