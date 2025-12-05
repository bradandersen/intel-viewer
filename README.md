# Intel Viewer

> Competitive Intelligence Dashboard for DLP/DSPM/Browser Security Market

A comprehensive toolkit for tracking 33+ competitors across Data Loss Prevention (DLP), Data Security Posture Management (DSPM), and Browser Security markets. Includes automated RSS aggregation, Excel tracker generation, and Google Alerts configuration.

![Market Coverage](https://img.shields.io/badge/Competitors-33+-blue)
![Categories](https://img.shields.io/badge/Categories-8-green)
![Alerts](https://img.shields.io/badge/Google_Alerts-22-orange)

## 🎯 Features

### 📊 Interactive Dashboard
- **Real-time RSS feed aggregation** from 36 sources
- **Expandable competitor lists** with color-coded tags
- **Search & filter** by keyword
- **Auto-refresh** every 30 minutes

### 📈 Excel Tracker Generator
Creates comprehensive workbook with 5 sheets:
- **Competitor Overview**: 33 companies with funding, valuation, employee data
- **News & Updates**: Track competitive intelligence chronologically
- **Product Comparison Matrix**: 18 competitors across 19 feature categories
- **Win-Loss Analysis**: Document deal outcomes and lessons learned
- **Battlecards**: Quick reference positioning for 13 key competitors

### 📢 Google Alerts Guide
Generates Word document with:
- 22 pre-configured competitor alert queries
- Market trend monitoring (Shadow AI, DSPM, AI Security)
- Funding & M&A tracking
- Best practices for alert management

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Modern web browser

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/intel-viewer.git
cd intel-viewer

# Install Python dependencies
pip install openpyxl python-docx

# Configure API key
cp config.example.js config.js
# Edit config.js and add your RSS2JSON API key from https://rss2json.com
```

### Usage

```bash
# Generate Excel tracker
python create_tracker.py
# Output: competitive_intelligence_tracker.xlsx

# Generate Google Alerts guide
python create_alerts_guide.py
# Output: google_alerts_configuration_guide.docx

# Open dashboard
open competitive_intelligence_dashboard.html
```

## 📋 Competitor Coverage

### Categories (33 competitors)

**Traditional DLP** (6)
- Nightfall AI, Varonis, Forcepoint, Digital Guardian, Proofpoint, Symantec

**DSPM** (7)
- Cyera, BigID, Sentra, Normalyze, Laminar, Dig Security, Polar Security

**CASB/SASE** (3)
- Netskope, Zscaler, Skyhigh Security

**Cloud Security** (3)
- Wiz, Lacework, Orca Security

**Endpoint/EDR** (3)
- CrowdStrike, SentinelOne, Code42

**Browser Security/BDR** (7)
- SquareX, Island, Talon/Palo Alto, LayerX, Seraphic, Surf, Menlo

**AI Security** (1)
- Lakera

**Other** (3)
- Veza (Identity/Access), Microsoft Purview (Compliance), Securiti.ai (Privacy)

## 🔧 Customization

### Add New Competitors

**1. Update tracker script** (`create_tracker.py`):
```python
["Company Name", "Category", "2024", "Location", "Series B", "$50M",
 "Series B", "2024", "$200M", "100-200", "Product Name", "Cloud SaaS",
 "Use cases", "Differentiators", "https://company.com",
 datetime.now().strftime("%Y-%m-%d")]
```

**2. Add Google Alert** (`create_alerts_guide.py`):
```python
('Company Name', 'CompanyName ("keyword" OR DLP) -jobs')
```

**3. Add RSS Feed** (`competitive_intelligence_dashboard.html`):
```javascript
{
    name: 'Company Name',
    tag: 'companytag',
    feeds: ['https://www.company.com/blog/rss.xml']
}
```

**4. Add color tag** (in `<style>` section):
```css
.tag-companytag { background: #e3f2fd; color: #1976d2; }
```

## 📁 Project Structure

```
intel-viewer/
├── competitive_intelligence_dashboard.html  # Interactive RSS dashboard
├── create_tracker.py                        # Excel generator
├── create_alerts_guide.py                   # Word doc generator
├── config.example.js                        # API key template
├── config.js                                # API key (gitignored)
├── README.md                                # This file
└── .gitignore                               # Git ignore rules
```

## 🔐 Security

- **API keys** are stored in `config.js` (not committed to repo)
- Use `config.example.js` as template
- Get free API key from [rss2json.com](https://rss2json.com)

## 📊 Product Comparison Matrix Features

The Excel tracker includes detailed feature comparison across:
- Shadow AI Detection
- GenAI Data Leakage Prevention
- Cloud-Native DLP
- Browser DLP (new category)
- Endpoint DLP
- Data Discovery & Classification
- Access Governance
- Autonomous Investigation
- Browser Agnostic capability
- Deployment Time
- Pricing Models

## 🎯 Use Cases

### Sales Enablement
- Review battlecards before customer calls
- Compare feature matrices during demos
- Track competitive win/loss patterns

### Product Strategy
- Monitor competitor product launches
- Identify feature gaps
- Track market trends (Shadow AI, GenAI security)

### Marketing Intelligence
- Stay updated on competitor messaging
- Track funding announcements
- Monitor market consolidation (M&A)

### Executive Reporting
- Weekly competitive intelligence summaries
- Market trend analysis
- Competitor valuation tracking

## 🛠️ Troubleshooting

### RSS feeds not loading
- Verify API key in `config.js`
- Check browser console for errors
- Some feeds may have CORS restrictions

### Excel generation errors
```bash
pip install --upgrade openpyxl python-docx
```

### Dashboard not showing competitors
- Ensure `config.js` exists (copy from `config.example.js`)
- Check browser supports ES6 JavaScript
- Open browser DevTools console for errors

## 📝 Contributing

Contributions welcome! To add competitors:
1. Fork the repository
2. Add competitor to all 3 files (tracker, alerts, dashboard)
3. Update this README
4. Submit pull request

## 📜 License

MIT License - feel free to use for competitive intelligence tracking

## 🙏 Acknowledgments

Built with Claude 3.5 Sonnet for automated competitive intelligence tracking in the DLP/DSPM/Browser Security market.

---

**Last Updated**: December 2024
**Competitors Tracked**: 33
**Google Alerts Configured**: 22
**RSS Sources**: 36
