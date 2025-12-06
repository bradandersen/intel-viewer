#!/usr/bin/env python3
"""
Automated Competitor Intelligence Gatherer

This script takes company names from companies.json and automatically:
1. Finds company websites and RSS feeds
2. Gathers business intelligence (funding, employees, HQ, etc.)
3. Updates all tracker files (Excel, HTML dashboard, Google Alerts)

Usage:
    python add_competitors.py                    # Process all new companies
    python add_competitors.py --company "Acme"   # Process specific company
    python add_competitors.py --rebuild          # Rebuild all files from config
"""

import json
import re
import time
import argparse
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import subprocess


class CompetitorResearcher:
    """Researches competitor information using Claude CLI."""

    def __init__(self):
        self.data_cache = {}
        self.load_existing_data()

    def load_existing_data(self):
        """Load existing competitor data to avoid re-research."""
        try:
            with open('competitor_data.json', 'r') as f:
                self.data_cache = json.load(f)
        except FileNotFoundError:
            self.data_cache = {}

    def save_data_cache(self):
        """Save researched data to cache file."""
        with open('competitor_data.json', 'w') as f:
            json.dump(self.data_cache, f, indent=2)

    def research_company(self, company_name: str, category: str) -> Dict:
        """
        Research a company using web search.

        Returns a dict with:
        - name, category, founded, headquarters, funding_stage, total_funding,
        - last_round, last_round_date, valuation, employees, products,
        - deployment, use_cases, differentiators, website, rss_feeds
        """
        # Check cache first
        if company_name in self.data_cache:
            print(f"✓ Using cached data for {company_name}")
            return self.data_cache[company_name]

        print(f"\n🔍 Researching {company_name}...")

        # This is where we'd use Claude or web APIs
        # For now, return a template that Claude can fill in
        data = {
            "name": company_name,
            "category": category,
            "founded": "TBD",
            "headquarters": "TBD",
            "funding_stage": "TBD",
            "total_funding": "TBD",
            "last_round": "TBD",
            "last_round_date": "TBD",
            "valuation": "TBD",
            "employees": "TBD",
            "products": "TBD",
            "deployment": "Cloud SaaS",
            "use_cases": "TBD",
            "differentiators": "TBD",
            "website": f"https://www.{company_name.lower().replace(' ', '')}.com",
            "rss_feeds": [],
            "last_updated": datetime.now().strftime("%Y-%m-%d")
        }

        # Cache the result
        self.data_cache[company_name] = data
        self.save_data_cache()

        return data

    def find_rss_feed(self, company_name: str, website: str) -> List[str]:
        """
        Attempt to find RSS feeds for a company.
        Returns list of potential RSS feed URLs.
        """
        feeds = []
        base_domain = website.replace('https://', '').replace('http://', '').split('/')[0]

        # Common RSS feed patterns
        patterns = [
            f"https://{base_domain}/blog/feed/",
            f"https://{base_domain}/feed/",
            f"https://{base_domain}/blog/rss.xml",
            f"https://{base_domain}/rss.xml",
            f"https://blog.{base_domain}/feed/",
            f"https://blog.{base_domain}/rss.xml",
        ]

        return patterns


class TrackerGenerator:
    """Generates tracker files from competitor data."""

    def __init__(self, researcher: CompetitorResearcher):
        self.researcher = researcher
        self.companies_config = self.load_companies_config()

    def load_companies_config(self) -> Dict:
        """Load companies.json configuration."""
        with open('companies.json', 'r') as f:
            return json.load(f)

    def generate_excel_data(self) -> List[List]:
        """Generate data rows for Excel tracker."""
        rows = []

        for category, companies in self.companies_config['categories'].items():
            for company_name in companies:
                data = self.researcher.research_company(company_name, category)

                row = [
                    data['name'],
                    data['category'],
                    data['founded'],
                    data['headquarters'],
                    data['funding_stage'],
                    data['total_funding'],
                    data['last_round'],
                    data['last_round_date'],
                    data['valuation'],
                    data['employees'],
                    data['products'],
                    data['deployment'],
                    data['use_cases'],
                    data['differentiators'],
                    data['website'],
                    data['last_updated']
                ]
                rows.append(row)

        return rows

    def generate_dashboard_feeds(self) -> List[Dict]:
        """Generate RSS feed configuration for HTML dashboard."""
        feeds = []

        for category, companies in self.companies_config['categories'].items():
            for company_name in companies:
                data = self.researcher.research_company(company_name, category)

                # Generate tag from company name
                tag = company_name.lower().replace(' ', '').replace('.', '')

                # Get RSS feeds and always add Google News
                rss_feeds = data.get('rss_feeds', []).copy()

                # Always add Google News as additional source
                search_terms = self._get_search_terms(company_name, category)
                google_news_url = f'https://news.google.com/rss/search?q={search_terms.replace(" ", "+")}&hl=en-US&gl=US&ceid=US:en'

                # Add Google News if not already present
                if not any('news.google.com' in feed for feed in rss_feeds):
                    rss_feeds.append(google_news_url)

                feed_config = {
                    'name': company_name,
                    'tag': tag,
                    'feeds': rss_feeds if rss_feeds else [google_news_url]
                }
                feeds.append(feed_config)

        return feeds

    def generate_google_alerts(self) -> List[Tuple[str, str]]:
        """Generate Google Alerts configuration."""
        alerts = []

        for category, companies in self.companies_config['categories'].items():
            for company_name in companies:
                search_terms = self._get_search_terms(company_name, category)
                alerts.append((company_name, search_terms))

        return alerts

    def _get_search_terms(self, company_name: str, category: str) -> str:
        """Generate appropriate search terms based on category."""
        # Base terms by category
        category_terms = {
            'DLP': 'DLP OR "data loss prevention"',
            'DSPM': 'DSPM OR "data security"',
            'CASB/SASE': 'CASB OR SASE OR DLP',
            'Cloud Security': '"cloud security" OR DSPM',
            'Endpoint/EDR': 'EDR OR "endpoint security" OR DLP',
            'Browser Security': '"browser security" OR DLP',
            'Workflow/BPM': 'workflow OR BPM OR automation',
            'AI Security': '"AI security" OR "LLM security"',
            'Other': 'security'
        }

        terms = category_terms.get(category, 'security')

        # Add company name with quotes if it has spaces
        if ' ' in company_name:
            company_query = f'"{company_name}"'
        else:
            company_query = company_name

        return f'{company_query} ({terms}) -jobs'

    def generate_css_tags(self) -> List[str]:
        """Generate CSS color tags for companies."""
        # Color palette for tags
        colors = [
            ('#e3f2fd', '#1976d2'),  # Blue
            ('#f3e5f5', '#7b1fa2'),  # Purple
            ('#fff3e0', '#ef6c00'),  # Orange
            ('#e8f5e9', '#388e3c'),  # Green
            ('#e0f2f1', '#00695c'),  # Teal
            ('#fce4ec', '#c2185b'),  # Pink
            ('#f1f8e9', '#558b2f'),  # Light Green
            ('#e8eaf6', '#3949ab'),  # Indigo
            ('#fff9c4', '#f57f17'),  # Yellow
            ('#e1f5fe', '#0277bd'),  # Light Blue
        ]

        css_rules = []
        color_index = 0

        for category, companies in self.companies_config['categories'].items():
            for company_name in companies:
                tag = company_name.lower().replace(' ', '').replace('.', '')
                bg, fg = colors[color_index % len(colors)]
                css_rules.append(f'.tag-{tag} {{ background: {bg}; color: {fg}; }}')
                color_index += 1

        return css_rules

    def update_excel_tracker(self):
        """Update create_tracker.py with new competitor data."""
        print("\n📊 Updating Excel tracker...")

        rows = self.generate_excel_data()

        # Read the existing file
        with open('create_tracker.py', 'r') as f:
            content = f.read()

        # Generate Python code for competitors list
        competitors_code = "competitors = [\n"
        for row in rows:
            # Format each field, handling None values
            formatted_row = []
            for field in row:
                if field == "TBD" or field is None:
                    formatted_row.append('"TBD"')
                elif isinstance(field, str):
                    # Escape quotes in strings
                    escaped = field.replace('"', '\\"')
                    formatted_row.append(f'"{escaped}"')
                else:
                    formatted_row.append(str(field))

            # Create the row with datetime handling
            competitors_code += f"    [{', '.join(formatted_row[:-1])}, datetime.now().strftime('%Y-%m-%d')],\n"

        competitors_code += "]"

        # Replace the competitors array
        pattern = r'competitors = \[.*?\]'
        new_content = re.sub(pattern, competitors_code, content, flags=re.DOTALL)

        # Write back
        with open('create_tracker.py', 'w') as f:
            f.write(new_content)

        print("✓ Excel tracker updated")

    def update_html_dashboard(self):
        """Update HTML dashboard with new RSS feeds and CSS."""
        print("\n🌐 Updating HTML dashboard...")

        feeds = self.generate_dashboard_feeds()
        css_tags = self.generate_css_tags()

        # Read existing file
        with open('competitive_intelligence_dashboard.html', 'r') as f:
            content = f.read()

        # Generate JavaScript for feeds
        feeds_js = "const competitorFeeds = [\n"
        for feed in feeds:
            feeds_js += "            {\n"
            feeds_js += f"                name: '{feed['name']}',\n"
            feeds_js += f"                tag: '{feed['tag']}',\n"
            feeds_js += "                feeds: [\n"
            for feed_url in feed['feeds']:
                feeds_js += f"                    '{feed_url}',\n"
            feeds_js += "                ]\n"
            feeds_js += "            },\n"
        feeds_js += "        ];"

        # Replace competitorFeeds array
        pattern = r'const competitorFeeds = \[.*?\];'
        content = re.sub(pattern, feeds_js, content, flags=re.DOTALL)

        # Generate and replace getCategoryForCompany categories object
        categories_js = "const categories = {\n"
        for category, companies in self.companies_config['categories'].items():
            companies_list = "', '".join(companies)
            categories_js += f"                '{category}': ['{companies_list}'],\n"
        categories_js += "            };"

        # Replace categories object in getCategoryForCompany function
        category_pattern = r'const categories = \{[^}]+\};'
        content = re.sub(category_pattern, categories_js, content, flags=re.DOTALL)

        # Generate and insert CSS tags
        css_section = '\n        '.join(css_tags)

        # Find and replace CSS tag section
        # This assumes there's a section with .tag- classes
        css_pattern = r'(\.tag-\w+\s*{[^}]+}\s*)+'
        if re.search(css_pattern, content):
            content = re.sub(css_pattern, css_section + '\n        ', content)

        # Write back
        with open('competitive_intelligence_dashboard.html', 'w') as f:
            f.write(content)

        print("✓ HTML dashboard updated")

    def update_alerts_guide(self):
        """Update Google Alerts guide with new competitors."""
        print("\n📢 Updating Google Alerts guide...")

        alerts = self.generate_google_alerts()

        # Read existing file
        with open('create_alerts_guide.py', 'r') as f:
            content = f.read()

        # Generate Python list for competitors
        alerts_code = "competitors_list = [\n"
        for company, query in alerts:
            alerts_code += f"    ('{company}', '{query}'),\n"
        alerts_code += "]"

        # Replace competitors_list
        pattern = r'competitors_list = \[.*?\]'
        content = re.sub(pattern, alerts_code, content, flags=re.DOTALL)

        # Write back
        with open('create_alerts_guide.py', 'w') as f:
            f.write(content)

        print("✓ Google Alerts guide updated")

    def update_readme(self):
        """Update README with accurate counts."""
        print("\n📝 Updating README...")

        # Count totals
        total_companies = sum(len(companies) for companies in self.companies_config['categories'].values())
        total_categories = len(self.companies_config['categories'])

        with open('README.md', 'r') as f:
            content = f.read()

        # Update badges
        content = re.sub(
            r'Competitors-\d+',
            f'Competitors-{total_companies}',
            content
        )
        content = re.sub(
            r'Categories-\d+',
            f'Categories-{total_categories}',
            content
        )
        content = re.sub(
            r'Google_Alerts-\d+',
            f'Google_Alerts-{total_companies}',
            content
        )

        # Update text mentions
        content = re.sub(
            r'tracking \d+\+ competitors',
            f'tracking {total_companies}+ competitors',
            content
        )
        content = re.sub(
            r'\d+ companies with funding',
            f'{total_companies} companies with funding',
            content
        )
        content = re.sub(
            r'Competitors Tracked\*\*: \d+',
            f'Competitors Tracked**: {total_companies}',
            content
        )
        content = re.sub(
            r'Google Alerts Configured\*\*: \d+',
            f'Google Alerts Configured**: {total_companies}',
            content
        )

        with open('README.md', 'w') as f:
            f.write(content)

        print("✓ README updated")


def main():
    parser = argparse.ArgumentParser(description='Automated Competitor Intelligence System')
    parser.add_argument('--company', help='Research specific company')
    parser.add_argument('--rebuild', action='store_true', help='Rebuild all files from config')
    parser.add_argument('--research-only', action='store_true', help='Only research companies, don\'t update files')

    args = parser.parse_args()

    print("🚀 Competitive Intelligence Automation System")
    print("=" * 50)

    researcher = CompetitorResearcher()
    generator = TrackerGenerator(researcher)

    if args.company:
        # Research single company
        print(f"\nResearching {args.company}...")
        data = researcher.research_company(args.company, "Unknown")
        print(json.dumps(data, indent=2))

    elif args.research_only:
        # Just research all companies
        print("\nResearching all companies...")
        for category, companies in generator.companies_config['categories'].items():
            print(f"\n📁 {category}")
            for company in companies:
                researcher.research_company(company, category)

    else:
        # Full rebuild
        print("\n🔨 Rebuilding all tracker files...\n")

        # Update all files
        generator.update_excel_tracker()
        generator.update_html_dashboard()
        generator.update_alerts_guide()
        generator.update_readme()

        print("\n✅ All files updated successfully!")
        print("\nNext steps:")
        print("1. Review competitor_data.json and fill in 'TBD' fields")
        print("2. Run 'python create_tracker.py' to generate Excel file")
        print("3. Run 'python create_alerts_guide.py' to generate Word doc")
        print("4. Open competitive_intelligence_dashboard.html to view dashboard")


if __name__ == '__main__':
    main()
