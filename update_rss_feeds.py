#!/usr/bin/env python3
"""Update RSS feeds in competitor_data.json"""

import json

# RSS feeds found through web search and verified
# Note: Many companies have disabled RSS feeds or moved them. Only working feeds are listed.
rss_feeds = {
    # Working RSS feeds
    "Varonis": ["https://www.varonis.com/blog/feed"],
    "Netskope": ["https://www.netskope.com/feed"],
    "Camunda": ["https://camunda.com/feed/"],
    "ProcessMaker": ["https://www.processmaker.com/blog/feed/"],
    "Zscaler": ["https://www.zscaler.com/blogs/feeds/security-research"],
    "Wiz": ["https://www.wiz.io/blog/rss"],
    "CrowdStrike": ["https://www.crowdstrike.com/blog/feed/"],
    "LayerX Security": ["https://www.layerxsecurity.com/blog/feed"],
    "Workato": ["https://www.workato.com/blog/feed/"],

    # RSS feeds disabled or returning 404 (verified 2025-12-05):
    # "Nightfall AI": [],  # 404 - no RSS feed available
    # "Cyera": [],  # 404 - no RSS feed available
    # "Sentra": [],  # 404 - no RSS feed available
    # "BigID": [],  # Returns HTML, not RSS
    # "Code42": [],  # 404 - no RSS feed available
    # "Island": [],  # 404 - no RSS feed available
    # "Seraphic Security": [],  # 404 - no RSS feed available
    # "Surf Security": [],  # 404 - no RSS feed available
    # "Menlo Security": [],  # 404 - no RSS feed available
    # "Appian": [],  # 404 - no RSS feed available
    # "Nintex": [],  # 404 - no RSS feed available
    # "Bizagi": [],  # 404 - no RSS feed available
    # "Flowable": [],  # 404 - no RSS feed available
}

# Load competitor data
with open('competitor_data.json', 'r') as f:
    data = json.load(f)

# Update RSS feeds
updated_count = 0
for company, feeds in rss_feeds.items():
    if company in data:
        data[company]["rss_feeds"] = feeds
        updated_count += 1
        print(f"✓ Updated {company}")
    else:
        print(f"✗ Company not found: {company}")

# Save updated data
with open('competitor_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n✅ Updated RSS feeds for {updated_count} companies")
print("Run 'python add_competitors.py --rebuild' to regenerate the dashboard")
