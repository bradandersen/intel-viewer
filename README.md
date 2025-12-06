# Competitive Intelligence Tracker

![Competitors](https://img.shields.io/badge/Competitors-42-blue)
![Categories](https://img.shields.io/badge/Categories-5-green)
![Smart_Cache](https://img.shields.io/badge/Smart_Cache-Enabled-orange)

Real-time competitive intelligence dashboard tracking 45 companies across DLP, DSPM, Browser Security, and Workflow/BPM markets with smart caching and automated feed aggregation.

## 🎯 Key Features

### **Smart Caching System**
- **Per-feed timestamps** - Each company tracks its own last update
- **1-hour intelligent refresh** - Only fetches stale feeds
- **Instant loading** - Uses localStorage cache for immediate display
- **Rate limit protection** - Avoids API throttling with smart delays

### **Live Dashboard**
- **90+ RSS feeds** - Company blogs + Google News for all competitors
- **Category navigation** - Jump to any of 9 market categories
- **Dual feed display** - Company blog posts first, then Google News
- **Search & filter** - Find news across all sources
- **Mobile responsive** - Works on desktop, tablet, and mobile
- **Per-feed refresh** - Individual refresh buttons for each company

### **Automation Suite**
- `add_competitors.py` - Rebuild dashboard from config
- `update_rss_feeds.py` - Add RSS feed URLs
- `create_tracker.py` - Generate Excel tracker
- `create_alerts_guide.py` - Generate Google Alerts guide

## 🚀 Quick Start

```bash
# Open the dashboard
open competitive_intelligence_dashboard.html

# First load: ~90 seconds (fetches all feeds)
# Subsequent loads: Instant (from cache)
```

### Optional: Configure API Key

Get free key from [rss2json.com](https://rss2json.com):

1. Copy `config.example.js` → `config.js`
2. Add your API key
3. Enjoy higher rate limits

## 📊 Dashboard Features

### **Refresh Button Intelligence**
```
🔄 Refresh Feeds
11 feeds ready to refresh (oldest: 1h)
```

- Shows how many feeds need updating
- Disabled until feeds are >1 hour old
- Only fetches stale feeds, uses cache for fresh ones

### **Per-Feed Status**
Each company shows:
```
Camunda
Last updated: 15m ago

🔗 COMPANY BLOG
[Blog posts...]

📰 GOOGLE NEWS
[News articles...]
```

### **Rate Limit Handling**
```
⚠️ Rate Limited
RSS2JSON API rate limit reached.
Wait a few minutes and refresh.
```

## 📁 Project Structure

```
├── competitive_intelligence_dashboard.html  # Main dashboard
├── companies.json                           # Company list by category
├── competitor_data.json                     # Company data cache
├── config.js                                # API key (gitignored)
├── add_competitors.py                       # Automation script
├── update_rss_feeds.py                      # RSS feed updater
├── create_tracker.py                        # Excel generator
└── create_alerts_guide.py                   # Google Alerts generator
```

## 🏢 Tracked Companies (45)

### **DLP** (6)
Nightfall AI, Varonis, Forcepoint, Digital Guardian, Proofpoint, Symantec

### **DSPM** (8)
Cyera, BigID, Sentra, Normalyze, Laminar, Dig Security, Polar Security, Securiti.ai

### **Browser Security** (7)
SquareX, Island, Talon, LayerX, Seraphic, Surf, Menlo

### **Workflow/BPM** (12)
Automation Anywhere, UiPath, Blue Prism, Microsoft Power Automate, Camunda, ProcessMaker, Appian, Pega, Nintex, Bizagi, Flowable, Workato

### **CASB/SASE** (3)
Netskope, Zscaler, Skyhigh Security

### **Cloud Security** (3)
Wiz, Lacework, Orca Security

### **Endpoint/EDR** (3)
CrowdStrike, SentinelOne, Code42

### **AI Security** (1)
Lakera

### **Other** (2)
Veza, Microsoft Purview

## 🔧 Adding New Competitors

### 1. Edit companies.json
```json
{
  "categories": {
    "DLP": ["Nightfall AI", "Varonis", "NewCompany"]
  }
}
```

### 2. Update RSS feeds (optional)
```bash
python update_rss_feeds.py
```

### 3. Rebuild dashboard
```bash
python add_competitors.py --rebuild
```

### 4. Generate outputs
```bash
python create_tracker.py           # Excel file
python create_alerts_guide.py      # Word doc
```

## 🛠️ Technical Details

### **Caching**
- Browser localStorage
- Per-feed timestamps
- 1-hour cache duration
- Survives page reloads

### **Rate Limiting**
- 1-second delay between API calls
- Skips recently updated feeds
- Progress indicator during fetch
- Graceful 429 error handling

### **Feed Processing**
- 5 items per feed
- HTML stripped from descriptions
- Date parsing and formatting
- Blog + Google News separation

## 📈 Statistics

- **Total Feeds**: 90+ (blog RSS + Google News)
- **Companies with Direct RSS**: 9 (verified working)
- **News Items**: ~450+ (varies by freshness)
- **Cache Hit Rate**: ~100% on repeated loads
- **First Load Time**: ~90 seconds (initial fetch)
- **Cached Load Time**: <1 second
- **Failed RSS Feeds**: 13 companies (404 errors, disabled by vendors)

## 🎨 Color-Coded Categories

Each company has a unique color tag for quick visual identification across the dashboard.

## 🔒 Privacy & Git

`.gitignore` excludes:
- `config.js` (API key)
- `*.xlsx` (generated files)
- `*.docx` (generated files)
- Generated tracker files

Safe to commit:
- `companies.json`
- `competitor_data.json`
- All `.py` scripts
- Dashboard HTML

## 📝 License

Personal project for competitive intelligence tracking.

---

**Built with:** Vanilla JavaScript, Python, RSS2JSON API
**Last Updated:** December 2025
