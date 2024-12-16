import requests
import time
import telegram

# 블록체인 API 및 텔레그램 봇 설정
BLOCKCHAIN_API_URL = 'https://api.blockchain.info/haskoin-store/btc/address/{address}/balance'
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID'

# 지갑 주소 설정
wallet_address = '0x97f1f8003ad0fb1c99361170310c65dc84f921e3'

# 텔레그램 봇 초기화
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

def get_wallet_balance(address):
    response = requests.get(BLOCKCHAIN_API_URL.format(address=address))
    balance_data = response.json()
    return balance_data['confirmed']

def send_telegram_message(message):
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

def track_wallet():
    previous_balance = get_wallet_balance(wallet_address)
    while True:
        current_balance = get_wallet_balance(wallet_address)
        if current_balance != previous_balance:
            message = f"지갑 잔액이 변경되었습니다. 이전: {previous_balance} BTC, 현재: {current_balance} BTC"
            send_telegram_message(message)
            previous_balance = current_balance
        time.sleep(300)  # 5분마다 잔액 확인

if __name__ == '__main__':
    track_wallet()
