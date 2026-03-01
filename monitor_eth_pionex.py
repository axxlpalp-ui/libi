#!/usr/bin/env python3
"""ETH Price Monitor - Pionex Version"""

import json
import urllib.request
import time
import os

# 你的設定
TARGET_PRICE = 1880   # 進場目標
STOP_LOSS = 1889.10   # 強平價 (Pionex)
PROFIT_1 = 1850
PROFIT_2 = 1800
PROFIT_3 = 1700
PROFIT_4 = 1600

NOTIFIED = {
    'entry': False,
    'stop_loss': False,
    'profit1': False,
    'profit2': False,
    'profit3': False,
    'profit4': False
}

def get_price_pionex():
    """從 Pionex 獲取價格"""
    try:
        # Pionex API
        url = "https://api.pionex.com/api/v1/ticker/24hr?symbol=ETH_USDT"
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read().decode())
            if data['code'] == 0:
                return float(data['data']['lastPrice'])
    except:
        pass
    
    # 備用 Binance
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read().decode())
            return float(data['price'])
    except:
        return None

def main():
    print("🚀 ETH 價格監控啟動！（Pionex）")
    print(f"進場目標: ${TARGET_PRICE}")
    print(f"強平價: ${STOP_LOSS}")
    print(f"目標: ${PROFIT_1} / ${PROFIT_2} / ${PROFIT_3} / ${PROFIT_4}")
    print("-" * 40)
    
    while True:
        price = get_price_pionex()
        if price:
            print(f"\r[{time.strftime('%H:%M:%S')}] ETH: ${price:.2f}", end="")
            
            # 進場通知
            if price <= TARGET_PRICE and not NOTIFIED['entry']:
                print(f"\n\n✅ 進場時機！ ${price:.2f} <= ${TARGET_PRICE}")
                NOTIFIED['entry'] = True
            
            # 止損通知
            if price >= STOP_LOSS and not NOTIFIED['stop_loss']:
                print(f"\n\n⚠️ 強平警告！ ${price:.2f} >= ${STOP_LOSS}")
                NOTIFIED['stop_loss'] = True
            
            # 獲利通知
            if price <= PROFIT_1 and not NOTIFIED['profit1']:
                print(f"\n\n🎉 目標1達成！ ${price:.2f} <= ${PROFIT_1}")
                NOTIFIED['profit1'] = True
                
            if price <= PROFIT_2 and not NOTIFIED['profit2']:
                print(f"\n\n🎉 目標2達成！ ${price:.2f} <= ${PROFIT_2}")
                NOTIFIED['profit2'] = True
                
            if price <= PROFIT_3 and not NOTIFIED['profit3']:
                print(f"\n\n🎉 目標3達成！ ${price:.2f} <= ${PROFIT_3}")
                NOTIFIED['profit3'] = True
            
            if price <= PROFIT_4 and not NOTIFIED['profit4']:
                print(f"\n\n🎉 目標4達成！ ${price:.2f} <= ${PROFIT_4}")
                NOTIFIED['profit4'] = True
        
        time.sleep(10)

if __name__ == "__main__":
    main()
