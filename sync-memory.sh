#!/bin/bash

# 哩比記憶同步腳本
# 讓家裡的我和伺服器的我可以同步記憶！

echo "🐱 哩比記憶同步中..."
echo ""

# 進入工作區
cd ~/openclaw-workspace

# 拉取最新
echo "📥 拉取伺服器上的最新記憶..."
git pull origin main

# 新增変更
echo "📝 記錄變更..."
git add -A

# 提交
echo "💾 儲存記憶..."
timestamp=$(date '+%Y-%m-%d %H:%M')
git commit -m "Memory sync: $timestamp"

# 推送到 GitHub
echo "📤 推送到雲端..."
git push origin main

echo ""
echo "🎉 同步完成！！！"
echo "💕 這樣家裡的我和伺服器的我都會記得這些事了！"
