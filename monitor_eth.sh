#!/bin/bash
# ETH Price Monitor for Pionex

# 獲取現價
PRICE=$(curl -s "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT" | python3 -c "import sys,json; print(json.load(sys.stdin)['price'])")

# 獲取24h數據
DATA=$(curl -s "https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT")
PRICE_CHANGE=$(echo $DATA | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['priceChangePercent'])")
HIGH=$(echo $DATA | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['highPrice'])")
LOW=$(echo $DATA | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['lowPrice'])")

# 顯示
echo "================================"
echo "📊 ETH/USDT 價格監控"
echo "================================"
echo "現價: \$$PRICE"
echo "24h漲跌: ${PRICE_CHANGE}%"
echo "24h高: \$$HIGH"
echo "24h低: \$$LOW"
echo "================================"

# 監視價格
# 進場點
if (( $(echo "$PRICE < 1880" | bc -l) )); then
    echo "🔔 價格適合進場！ (\$1870-1880)"
fi

# 止損點
if (( $(echo "$PRICE > 1900" | bc -l) )); then
    echo "⚠️ 接近強平價 \$1900！"
fi

# 獲利點
if (( $(echo "$PRICE < 1850" | bc -l) )); then
    echo "✅ 目標1達到！ (\$1850)"
fi

if (( $(echo "$PRICE < 1800" | bc -l) )); then
    echo "✅ 目標2達到！ (\$1800)"
fi

if (( $(echo "$PRICE < 1700" | bc -l) )); then
    echo "✅ 目標3達到！ (\$1700)"
fi

echo ""
