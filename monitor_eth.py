#!/usr/bin/env python3
"""ETH Price Monitor for Pionex"""

import json
import urllib.request
import sys

def get_price():
    url = "https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        return {
            'price': float(data['lastPrice']),
            'change': float(data['priceChangePercent']),
            'high': float(data['highPrice']),
            'low': float(data['lowPrice'])
        }

def main():
    print("=" * 40)
    print("📊 ETH/USDT 價格監控")
    print("=" * 40)
    
    try:
        p = get_price()
        print(f"現價: ${p['price']:.2f}")
        print(f"24h漲跌: {p['change']:.2f}%")
        print(f"24h高: ${p['high']:.2f}")
        print(f"24h低: ${p['low']:.2f}")
        print("=" * 40)
        
        price = p['price']
        
        # 監視點
        print("\n🎯 監視點:")
        
        # 進場
        if price < 1880:
            print(f"✅ 價格 ${price:.2f} 適合進場！(目標 <1880)")
        
        # 止損
        if price > 1890:
            print(f"⚠️ 接近強平價 $1900！")
        
        # 獲利
        if price < 1850:
            print(f"🎉 目標1達到！ $1850 (+{(1880-1850)/1880*100:.1f}%)")
        
        if price < 1800:
            print(f"🎉 目標2達到！ $1800 (+{(1880-1800)/1880*100:.1f}%)")
            
        if price < 1700:
            print(f"🎉 目標3達到！ $1700 (+{(1880-1700)/1880*100:.1f}%)")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
