#!/usr/bin/env python3
"""Update RSS feeds in competitor_data.json"""

import json

# RSS feeds found through web search
rss_feeds = {
    "Varonis": ["https://www.varonis.com/blog/feed"],
    "Netskope": ["https://www.netskope.com/feed"],
    "Camunda": ["https://camunda.com/feed/"],
    "ProcessMaker": ["https://www.processmaker.com/blog/feed/"],
    "Zscaler": ["https://www.zscaler.com/blogs/feeds/security-research"],
    "Wiz": ["https://www.wiz.io/blog/rss"],
    "Cyera": ["https://www.cyera.com/blog/feed"],
    "Nightfall AI": ["https://www.nightfall.ai/blog/feed"],
    "Code42": ["https://www.code42.com/blog/feed/"],
    "CrowdStrike": ["https://www.crowdstrike.com/blog/feed/"],
    "Sentra": ["https://www.sentra.io/blog/feed"],
    "BigID": ["https://bigid.com/blog/feed/"],
    "Island": ["https://www.island.io/blog/feed"],
    "LayerX Security": ["https://www.layerxsecurity.com/blog/feed"],
    "Seraphic Security": ["https://seraphicsecurity.com/blog/feed"],
    "Surf Security": ["https://www.surf.security/blog/feed"],
    "Menlo Security": ["https://www.menlosecurity.com/blog/feed/"],
    "Appian": ["https://www.appian.com/blog/feed/"],
    "Nintex": ["https://www.nintex.com/blog/feed/"],
    "Bizagi": ["https://www.bizagi.com/en/blog/feed"],
    "Flowable": ["https://www.flowable.com/blog/feed"],
    "Workato": ["https://www.workato.com/blog/feed/"],
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
