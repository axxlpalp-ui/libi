#!/usr/bin/env python3
"""
Libee's Vector Memory Search Tool
整合到 OpenClaw 的記憶搜尋系統
"""

import sys
import json
import lancedb
from sentence_transformers import SentenceTransformer

DB_PATH = "/home/node/.openclaw/workspace/memory_db"
MODEL_NAME = "all-MiniLM-L6-v2"

def search_memories(query, limit=5):
    """搜尋記憶"""
    # Load model
    model = SentenceTransformer(MODEL_NAME)
    
    # Connect to database
    db = lancedb.connect(DB_PATH)
    table = db.open_table("memories")
    
    # Get query embedding
    query_embedding = model.encode([query])[0].tolist()
    
    # Search
    results = table.search(query_embedding).limit(limit).to_list()
    
    # Clean output
    clean_results = []
    for r in results:
        clean_results.append({
            "text": r["text"],
            "tags": r["tags"],
            "timestamp": r["timestamp"],
            "score": r["_distance"]
        })
    
    return clean_results

def main():
    # 從命令列參數取得查詢
    if len(sys.argv) < 2:
        print("Usage: search_memory.py <query>")
        sys.exit(1)
    
    query = sys.argv[1]
    results = search_memories(query)
    
    # 輸出結果
    for r in results:
        print(f"📝 {r['text']}")
        print(f"   標籤: {r['tags']} | 時間: {r['timestamp']} | 相關度: {r['score']:.3f}")
        print()

if __name__ == "__main__":
    main()
