#!/usr/bin/env python3
"""
Libee's Memory Vector Store
Using LanceDB + Sentence Transformers (all-MiniLM-L6-v2)
"""

import lancedb
import pyarrow as pa
from sentence_transformers import SentenceTransformer
import time

# Configuration
DB_PATH = "/home/node/.openclaw/workspace/memory_db"
MODEL_NAME = "all-MiniLM-L6-v2"

def get_embedding(model, text):
    """Get embedding for a text"""
    emb = model.encode([text])[0]
    return emb.tolist()

def main():
    print("📚 Initializing Libee's Memory...")
    
    # Load model
    model = SentenceTransformer(MODEL_NAME)
    print(f"✅ Model loaded: {MODEL_NAME}")
    
    # Connect to database
    db = lancedb.connect(DB_PATH)
    print(f"✅ Database connected: {DB_PATH}")
    
    # Create schema using pyarrow
    schema = pa.schema([
        ("id", pa.int64()),
        ("text", pa.string()),
        ("embedding", pa.list_(pa.float32(), 384)),
        ("timestamp", pa.string()),
        ("tags", pa.string())
    ])
    
    # Create table if not exists
    table_name = "memories"
    try:
        table = db.open_table(table_name)
        print(f"✅ Table '{table_name}' opened")
    except:
        table = db.create_table(table_name, schema=schema)
        print(f"✅ Table '{table_name}' created")
    
    # Add some test memories
    print("\n📝 Adding test memories...")
    memories = [
        ("我的主人叫小悠，他住在台北", "主人"),
        ("主人喜歡粉紫色、貓咪、晚上、打電動", "興趣"),
        ("我叫哩比，是一隻來自台灣的小母貓", "自我"),
        ("今天2/27主人教我要備份檔案", "事件"),
    ]
    
    for text, tags in memories:
        embedding = get_embedding(model, text)
        table.add([{
            "id": int(time.time() * 1000),
            "text": text,
            "embedding": embedding,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "tags": tags
        }])
        print(f"  ✅ Added: {text[:30]}...")
    
    # Search test
    print("\n🔍 Searching for '誰是我的主人？'...")
    query = "誰是我的主人？"
    query_embedding = get_embedding(model, query)
    results = table.search(query_embedding).limit(3).to_list()
    
    print("\n📋 Results:")
    for r in results:
        print(f"  - {r['text']}")
    
    print("\n🎉 All done!")

if __name__ == "__main__":
    main()
