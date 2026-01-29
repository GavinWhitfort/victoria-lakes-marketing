#!/usr/bin/env python3
"""
Reddit Pain Point Scanner with Telegram Delivery
Scans Reddit and sends summary to Telegram
"""

import praw
import os
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
import re

load_dotenv()

# Same scanning logic as before
SUBREDDITS = [
    'Entrepreneur', 'SaaS', 'startups', 'indiehackers',
    'SideProject', 'smallbusiness', 'EntrepreneurRideAlong',
    'productivity', 'iOS', 'iphone', 'apple', 'androidapps',
    'webdev', 'programming', 'technology',
    'australia', 'melbourne', 'sydney', 'brisbane',
    'AusFinance', 'AusFishing', 'boating',
    'camping', 'hiking', 'Fishing', 'sailing',
    'personalfinance', 'dataisbeautiful', 'LifeProTips'
]

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

CATEGORIES = {
    'mobile_app': ['app', 'iphone', 'android', 'mobile', 'ios'],
    'web_tool': ['website', 'web', 'online', 'browser', 'tool'],
    'automation': ['automate', 'automatic', 'schedule', 'reminder'],
    'data_tracking': ['track', 'monitor', 'check', 'update', 'notification'],
    'productivity': ['organize', 'manage', 'plan', 'todo', 'calendar'],
    'finance': ['money', 'budget', 'price', 'cost', 'payment', 'invoice'],
    'local_services': ['near me', 'local', 'melbourne', 'sydney', 'australia'],
}

def matches_pain_pattern(text):
    text_lower = text.lower()
    for pattern in PAIN_PATTERNS:
        if re.search(pattern, text_lower):
            return True
    return False

def categorize_pain_point(text):
    text_lower = text.lower()
    categories = []
    for category, keywords in CATEGORIES.items():
        if any(keyword in text_lower for keyword in keywords):
            categories.append(category)
    return categories if categories else ['uncategorized']

def extract_pain_point(submission):
    return {
        'id': submission.id,
        'title': submission.title,
        'body': submission.selftext[:300] if submission.selftext else '',
        'subreddit': submission.subreddit.display_name,
        'url': f"https://reddit.com{submission.permalink}",
        'score': submission.score,
        'num_comments': submission.num_comments,
        'categories': categorize_pain_point(f"{submission.title} {submission.selftext}"),
    }

def scan_subreddits(reddit, hours_back=24):
    pain_points = []
    cutoff_time = datetime.now() - timedelta(hours=hours_back)
    
    for subreddit_name in SUBREDDITS:
        try:
            subreddit = reddit.subreddit(subreddit_name)
            for submission in subreddit.new(limit=30):
                post_time = datetime.fromtimestamp(submission.created_utc)
                if post_time < cutoff_time:
                    continue
                
                text = f"{submission.title} {submission.selftext}"
                if matches_pain_pattern(text):
                    pain_points.append(extract_pain_point(submission))
        except Exception as e:
            continue
    
    return pain_points

def format_telegram_message(pain_points):
    """Format pain points as Telegram message"""
    if not pain_points:
        return "🔍 **Daily Pain Point Scan**\n\nNo significant pain points found today."
    
    # Sort by score
    top_pain_points = sorted(pain_points, key=lambda x: x['score'], reverse=True)[:8]
    
    msg = f"🔍 **Daily Pain Point Scan**\n"
    msg += f"📅 {datetime.now().strftime('%Y-%m-%d')}\n"
    msg += f"📊 Found {len(pain_points)} pain points\n\n"
    msg += "🔥 **Top Opportunities:**\n\n"
    
    for i, pp in enumerate(top_pain_points, 1):
        # Truncate title if too long
        title = pp['title'][:80] + "..." if len(pp['title']) > 80 else pp['title']
        
        msg += f"{i}. **{title}**\n"
        msg += f"   r/{pp['subreddit']} | {pp['score']}↑ {pp['num_comments']}💬\n"
        
        # Add categories
        if pp['categories']:
            cats = ', '.join(pp['categories'][:2])
            msg += f"   🏷️ {cats}\n"
        
        msg += f"   🔗 {pp['url']}\n\n"
    
    # Save full report to file
    os.makedirs('pain_points', exist_ok=True)
    report_path = f"pain_points/report_{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(report_path, 'w') as f:
        json.dump(pain_points, f, indent=2)
    
    msg += f"\n📁 Full report: `{report_path}`"
    
    return msg

def main():
    print("🔍 Scanning Reddit for pain points...")
    
    # Connect to Reddit
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        username=os.getenv('REDDIT_USERNAME'),
        password=os.getenv('REDDIT_PASSWORD'),
        user_agent='PainPointScanner/1.0'
    )
    
    # Scan
    pain_points = scan_subreddits(reddit, hours_back=24)
    print(f"Found {len(pain_points)} pain points")
    
    # Format message
    message = format_telegram_message(pain_points)
    
    # Output for cron to send
    print("\n" + "="*60)
    print("TELEGRAM_MESSAGE:")
    print(message)
    print("="*60)
    
    # Also save message to file for cron to read
    with open('/tmp/pain_point_message.txt', 'w') as f:
        f.write(message)

if __name__ == '__main__':
    main()
