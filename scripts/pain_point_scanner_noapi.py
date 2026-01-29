#!/usr/bin/env python3
"""
Reddit Pain Point Scanner - No API Required
Scrapes Reddit via web for pain points
"""

import requests
import json
from datetime import datetime, timedelta
import re
import time

# Subreddits to monitor
SUBREDDITS = [
    'Entrepreneur', 'SaaS', 'startups', 'indiehackers',
    'SideProject', 'smallbusiness', 'productivity', 'iOS',
    'australia', 'melbourne', 'AusFishing', 'boating',
    'camping', 'Fishing'
]

PAIN_PATTERNS = [
    r"i wish (there was|i had|someone made)",
    r"why (doesn't|isn't there|can't i)",
    r"is there (an? app|a tool|a way)",
    r"does anyone know (an? app|a tool)",
    r"i hate (that|when|how)",
    r"it's so (annoying|frustrating|hard)",
    r"there should be",
    r"someone needs to (make|build|create)",
    r"tired of",
    r"sick of",
    r"looking for (an? app|a tool)",
    r"need (an? app|a tool|something)",
]

def matches_pain_pattern(text):
    text_lower = text.lower()
    for pattern in PAIN_PATTERNS:
        if re.search(pattern, text_lower):
            return True
    return False

def fetch_subreddit(subreddit, limit=25):
    """Fetch posts from subreddit via JSON endpoint"""
    url = f"https://www.reddit.com/r/{subreddit}/new.json?limit={limit}"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; PainPointScanner/1.0)'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('children', [])
        else:
            print(f"  ❌ Failed: HTTP {response.status_code}")
            return []
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return []

def extract_pain_point(post_data):
    """Extract pain point from Reddit post data"""
    data = post_data.get('data', {})
    
    return {
        'title': data.get('title', ''),
        'body': data.get('selftext', '')[:300],
        'subreddit': data.get('subreddit', ''),
        'url': f"https://reddit.com{data.get('permalink', '')}",
        'score': data.get('score', 0),
        'num_comments': data.get('num_comments', 0),
        'created': datetime.fromtimestamp(data.get('created_utc', 0)).isoformat(),
    }

def scan_subreddits(hours_back=24):
    """Scan subreddits for pain points"""
    print(f"🔍 Scanning {len(SUBREDDITS)} subreddits...\n")
    
    pain_points = []
    cutoff_time = datetime.now() - timedelta(hours=hours_back)
    
    for subreddit in SUBREDDITS:
        print(f"r/{subreddit}...", end=" ")
        posts = fetch_subreddit(subreddit)
        
        found_count = 0
        for post in posts:
            data = post.get('data', {})
            post_time = datetime.fromtimestamp(data.get('created_utc', 0))
            
            if post_time < cutoff_time:
                continue
            
            title = data.get('title', '')
            body = data.get('selftext', '')
            text = f"{title} {body}"
            
            if matches_pain_pattern(text):
                pain_points.append(extract_pain_point(post))
                found_count += 1
        
        print(f"✅ {found_count} found")
        time.sleep(2)  # Be polite to Reddit
    
    return pain_points

def format_telegram_message(pain_points):
    """Format for Telegram"""
    if not pain_points:
        return "🔍 **Daily Pain Point Scan**\n\nNo pain points found today."
    
    top_pain_points = sorted(pain_points, key=lambda x: x['score'], reverse=True)[:8]
    
    msg = f"🔍 **Daily Pain Point Scan**\n"
    msg += f"📅 {datetime.now().strftime('%Y-%m-%d')}\n"
    msg += f"📊 Found {len(pain_points)} pain points\n\n"
    msg += "🔥 **Top Opportunities:**\n\n"
    
    for i, pp in enumerate(top_pain_points, 1):
        title = pp['title'][:80] + "..." if len(pp['title']) > 80 else pp['title']
        
        msg += f"{i}. **{title}**\n"
        msg += f"   r/{pp['subreddit']} | {pp['score']}↑ {pp['num_comments']}💬\n"
        msg += f"   🔗 {pp['url']}\n\n"
    
    return msg

def main():
    print("🔍 Reddit Pain Point Scanner (No API)\n")
    print("=" * 60)
    
    # Scan
    pain_points = scan_subreddits(hours_back=24)
    print(f"\n✅ Found {len(pain_points)} pain points!\n")
    
    # Format message
    message = format_telegram_message(pain_points)
    
    # Save
    with open('/tmp/pain_point_message.txt', 'w') as f:
        f.write(message)
    
    print("=" * 60)
    print(message)
    print("=" * 60)
    
    print(f"\n✅ Saved to /tmp/pain_point_message.txt")

if __name__ == '__main__':
    main()
