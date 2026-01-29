#!/usr/bin/env python3
"""
Reddit Pain Point Scanner
Monitors subreddits for pain points, product ideas, and problems people need solved
"""

import praw
import os
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
import re

load_dotenv()

# Subreddits to monitor for pain points
SUBREDDITS = [
    # Entrepreneurship & SaaS
    'Entrepreneur', 'SaaS', 'startups', 'indiehackers',
    'SideProject', 'smallbusiness', 'EntrepreneurRideAlong',
    
    # Tech & Productivity
    'productivity', 'iOS', 'iphone', 'apple', 'androidapps',
    'webdev', 'programming', 'technology',
    
    # Local (Australia)
    'australia', 'melbourne', 'sydney', 'brisbane',
    'AusFinance', 'AusFishing', 'boating',
    
    # Specific niches
    'camping', 'hiking', 'Fishing', 'sailing',
    'personalfinance', 'dataisbeautiful', 'LifeProTips'
]

# Patterns that indicate pain points / product opportunities
PAIN_PATTERNS = [
    r"i wish (there was|i had|someone made)",
    r"why (doesn't|isn't there|can't i)",
    r"is there (an? app|a tool|a way|anything)",
    r"does anyone know (an? app|a tool|how to)",
    r"i hate (that|when|how)",
    r"it's so (annoying|frustrating|hard) (that|when|to)",
    r"there should be",
    r"someone needs to (make|build|create)",
    r"tired of (not having|checking|opening)",
    r"sick of (not having|checking|opening)",
    r"(why|how) is there (no|not a)",
    r"looking for (an? app|a tool|a way)",
    r"need (an? app|a tool|something)",
    r"can't believe there's no",
]

# Categories for pain points
CATEGORIES = {
    'mobile_app': ['app', 'iphone', 'android', 'mobile', 'ios'],
    'web_tool': ['website', 'web', 'online', 'browser', 'tool'],
    'automation': ['automate', 'automatic', 'schedule', 'reminder'],
    'data_tracking': ['track', 'monitor', 'check', 'update', 'notification'],
    'productivity': ['organize', 'manage', 'plan', 'todo', 'calendar'],
    'finance': ['money', 'budget', 'price', 'cost', 'payment', 'invoice'],
    'local_services': ['near me', 'local', 'melbourne', 'sydney', 'australia'],
}

LOG_FILE = 'pain_points/daily_log.json'
REPORT_FILE = 'pain_points/daily_report.md'

def load_pain_log():
    """Load existing pain points log"""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    return {'pain_points': [], 'last_scan': None}

def save_pain_log(log):
    """Save pain points log"""
    os.makedirs('pain_points', exist_ok=True)
    log['last_scan'] = datetime.now().isoformat()
    with open(LOG_FILE, 'w') as f:
        json.dump(log, f, indent=2)

def matches_pain_pattern(text):
    """Check if text contains pain point indicators"""
    text_lower = text.lower()
    for pattern in PAIN_PATTERNS:
        if re.search(pattern, text_lower):
            return True
    return False

def categorize_pain_point(text):
    """Categorize the pain point"""
    text_lower = text.lower()
    categories = []
    
    for category, keywords in CATEGORIES.items():
        if any(keyword in text_lower for keyword in keywords):
            categories.append(category)
    
    return categories if categories else ['uncategorized']

def extract_pain_point(submission):
    """Extract pain point details from submission"""
    return {
        'id': submission.id,
        'title': submission.title,
        'body': submission.selftext[:500] if submission.selftext else '',
        'subreddit': submission.subreddit.display_name,
        'url': f"https://reddit.com{submission.permalink}",
        'score': submission.score,
        'num_comments': submission.num_comments,
        'created': datetime.fromtimestamp(submission.created_utc).isoformat(),
        'categories': categorize_pain_point(f"{submission.title} {submission.selftext}"),
        'timestamp': datetime.now().isoformat()
    }

def scan_subreddits(reddit, hours_back=24):
    """Scan subreddits for pain points"""
    print(f"🔍 Scanning {len(SUBREDDITS)} subreddits for pain points...\n")
    
    pain_points = []
    cutoff_time = datetime.now() - timedelta(hours=hours_back)
    
    for subreddit_name in SUBREDDITS:
        try:
            print(f"Scanning r/{subreddit_name}...", end=" ")
            subreddit = reddit.subreddit(subreddit_name)
            
            found_count = 0
            for submission in subreddit.new(limit=50):
                # Check if post is recent
                post_time = datetime.fromtimestamp(submission.created_utc)
                if post_time < cutoff_time:
                    continue
                
                # Check title and body for pain patterns
                text = f"{submission.title} {submission.selftext}"
                if matches_pain_pattern(text):
                    pain_point = extract_pain_point(submission)
                    pain_points.append(pain_point)
                    found_count += 1
            
            print(f"✅ Found {found_count}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            continue
    
    return pain_points

def generate_daily_report(pain_points):
    """Generate markdown report of pain points"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Group by category
    by_category = {}
    for pp in pain_points:
        for cat in pp['categories']:
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(pp)
    
    # Sort by score (engagement)
    for cat in by_category:
        by_category[cat].sort(key=lambda x: x['score'], reverse=True)
    
    # Generate markdown
    report = f"""# Reddit Pain Points Report
**Date:** {today}
**Total Pain Points Found:** {len(pain_points)}

---

## 🔥 Hot Pain Points (High Engagement)

"""
    
    # Top 10 by score
    top_pain_points = sorted(pain_points, key=lambda x: x['score'], reverse=True)[:10]
    
    for i, pp in enumerate(top_pain_points, 1):
        report += f"""### {i}. {pp['title']}
- **Subreddit:** r/{pp['subreddit']}
- **Score:** {pp['score']} upvotes | {pp['num_comments']} comments
- **Category:** {', '.join(pp['categories'])}
- **URL:** {pp['url']}

**Excerpt:**
> {pp['body'][:300] if pp['body'] else '(Title only)'}

---

"""
    
    # By category
    report += "\n## 📊 Pain Points by Category\n\n"
    
    for category, items in sorted(by_category.items(), key=lambda x: len(x[1]), reverse=True):
        report += f"### {category.replace('_', ' ').title()} ({len(items)} found)\n\n"
        
        for pp in items[:5]:  # Top 5 per category
            report += f"- **[{pp['score']}↑]** {pp['title']} (r/{pp['subreddit']})\n"
            report += f"  {pp['url']}\n\n"
        
        report += "\n"
    
    # Save report
    os.makedirs('pain_points', exist_ok=True)
    report_path = f'pain_points/report_{today}.md'
    
    with open(report_path, 'w') as f:
        f.write(report)
    
    # Also save as latest
    with open(REPORT_FILE, 'w') as f:
        f.write(report)
    
    return report_path

def main():
    print("🔍 Reddit Pain Point Scanner\n")
    print("=" * 60)
    
    # Connect to Reddit
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        username=os.getenv('REDDIT_USERNAME'),
        password=os.getenv('REDDIT_PASSWORD'),
        user_agent='PainPointScanner/1.0'
    )
    
    # Load existing log
    log = load_pain_log()
    
    # Scan for pain points (last 24 hours)
    pain_points = scan_subreddits(reddit, hours_back=24)
    
    print(f"\n✅ Found {len(pain_points)} pain points!\n")
    
    # Filter out duplicates
    existing_ids = {pp['id'] for pp in log['pain_points']}
    new_pain_points = [pp for pp in pain_points if pp['id'] not in existing_ids]
    
    print(f"📊 {len(new_pain_points)} new pain points (filtered duplicates)\n")
    
    # Add to log
    log['pain_points'].extend(new_pain_points)
    
    # Keep only last 1000 pain points
    if len(log['pain_points']) > 1000:
        log['pain_points'] = log['pain_points'][-1000:]
    
    save_pain_log(log)
    
    # Generate report
    if pain_points:
        report_path = generate_daily_report(pain_points)
        print(f"📄 Report saved: {report_path}")
        print(f"📄 Latest: {REPORT_FILE}")
    else:
        print("No pain points found.")
    
    print("\n" + "=" * 60)
    print("✅ Scan complete!")

if __name__ == '__main__':
    main()
