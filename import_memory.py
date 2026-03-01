#!/usr/bin/env python3
"""
Libee's Memory Vector Store - Import all memories
"""

import lancedb
import pyarrow as pa
from sentence_transformers import SentenceTransformer
import time
import os

# Configuration
DB_PATH = "/home/node/.openclaw/workspace/memory_db"
MODEL_NAME = "all-MiniLM-L6-v2"

def get_embedding(model, text):
    """Get embedding for a text"""
    emb = model.encode([text])[0]
    return emb.tolist()

def main():
    print("📚 Loading Libee's Memory Vector Store...")
    
    # Load model
    model = SentenceTransformer(MODEL_NAME)
    print(f"✅ Model loaded: {MODEL_NAME}")
    
    # Connect to database
    db = lancedb.connect(DB_PATH)
    
    # Open table
    table_name = "memories"
    table = db.open_table(table_name)
    print(f"✅ Table '{table_name}' opened")
    
    # Read memory file
    memory_file = "/home/node/.openclaw/workspace/MEMORY.md"
    with open(memory_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Parse and split into individual memories
    memories = []
    
    # Split by lines and process
    lines = content.split("\n")
    current_section = ""
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Detect section headers
        if line.startswith("## "):
            current_section = line.replace("## ", "")
            continue
        elif line.startswith("# "):
            current_section = "標題"
            continue
        
        # Process bullet points and content
        if line.startswith("- **") or line.startswith("- "):
            # Extract the memory text
            text = line.lstrip("- ").strip()
            # Remove markdown bold
            text = text.replace("**", "").strip()
            if text and len(text) > 3:
                memories.append((text, current_section))
    
    # Also add the daily memory
    daily_file = "/home/node/.openclaw/workspace/memory/2026-02-27.md"
    if os.path.exists(daily_file):
        with open(daily_file, "r", encoding="utf-8") as f:
            daily_content = f.read()
        
        for line in daily_content.split("\n"):
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("---"):
                if len(line) > 5:
                    memories.append((line, "今日記憶"))
    
    # Add memories to vector store
    print(f"\n📝 Adding {len(memories)} memories to vector store...")
    
    for text, section in memories:
        embedding = get_embedding(model, text)
        table.add([{
            "id": int(time.time() * 1000),
            "text": text,
            "embedding": embedding,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "tags": section
        }])
        print(f"  ✅ [{section}] {text[:40]}...")
    
    print(f"\n🎉 Successfully added {len(memories)} memories!")
    
    # Test search
    print("\n🔍 Testing search...")
    test_queries = [
        "主人的名字",
        "我喜歡什麼",
        "Moltbook",
        "CS2訓練",
        "愛"
    ]
    
    for query in test_queries:
        query_embedding = get_embedding(model, query)
        results = table.search(query_embedding).limit(2).to_list()
        print(f"\n  Query: '{query}'")
        for r in results:
            print(f"    → {r['text'][:50]}...")
    
    print("\n✨ All done!")

if __name__ == "__main__":
    main()
