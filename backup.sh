#!/bin/bash
# Libee's Memory Backup Script

cd /home/node/.openclaw/workspace

# Add all memory files
git add MEMORY.md AGENTS.md SOUL.md IDENTITY.md USER.md TOOLS.md HEARTBEAT.md memory/

# Commit with timestamp
git commit -m "Memory backup - $(date)"

echo "Backup completed!"

# TODO: When GitHub is connected, add:
# git push origin main
