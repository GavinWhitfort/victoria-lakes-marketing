#!/usr/bin/env python3
"""
Reddit Lake Monitor Bot
Monitors Victorian subreddits for lake-related posts and provides helpful engagement
"""

import praw
import os
import json
import time
from datetime import datetime, timedelta

# Configuration
SUBREDDITS = [
    'melbourne',
    'australia', 
    'fishing_australia',
    'AusFishing',
    'boating',
    'Fishing',
    'camping',
    'Scriptable',
    'iOSsetups'
]

KEYWORDS = [
    'lake eildon', 'eildon', 
    'lake hume', 'hume dam',
    'lake nagambie', 'nagambie',
    'lake mulwala', 'mulwala',
    'lake buffalo', 'buffalo dam',
    'dartmouth dam',
    'lake eppalock',
    'water level', 'lake level',
    'scriptable widget', 'ios widget',
    'fishing victoria', 'vic fishing',
    'boating vic', 'boating victoria'
]

# Response templates (varied to seem natural)
RESPONSES = {
    'lake_level': [
        "I actually built a Scriptable widget for this! Shows live water levels for 22+ Victorian lakes (Eildon, Mulwala, Nagambie, etc.) right on your iPhone home screen. Tracks weekly trends too which is great for fishing. Check it out: {link}",
        
        "If you're checking lake levels regularly, I made a widget that might help - shows live data for Eildon, Hume, Nagambie and 20+ other Vic lakes on your iPhone. Has weekly change indicators so you can see if it's rising/falling. Link: {link}",
        
        "Fellow lake person here! I got tired of checking those clunky government websites so I built a widget for iPhone that shows live levels for Victorian lakes. Supports Eildon, Mulwala, Nagambie, Buffalo, Dartmouth + heaps more. Worth a look: {link}"
    ],
    
    'fishing': [
        "Pro tip: I track lake levels with a Scriptable widget on my iPhone - shows weekly rises/falls which helps predict bite windows. Works for 22 Victorian lakes including Eildon, Mulwala, Nagambie. Check it out: {link}",
        
        "If you fish Vic lakes regularly, this widget might be useful - live water levels + weekly trends for Eildon, Hume, Mulwala, etc. Helps plan trips around water movement. Link: {link}"
    ],
    
    'scriptable': [
        "I built a Victorian lakes water level widget for Scriptable if anyone's interested - 22 lakes supported (Eildon, Mulwala, Nagambie, etc.), three sizes, live data with weekly trends. Link: {link}",
        
        "Made a lakes widget for Scriptable - tracks water levels for 22+ Victorian lakes. Really useful for boating/fishing. Check it out: {link}"
    ]
}

LOG_FILE = 'logs/reddit_activity.json'

def load_activity_log():
    """Load previous activity to avoid duplicate comments"""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    return {'commented_posts': [], 'last_run': None}

def save_activity_log(log):
    """Save activity log"""
    os.makedirs('logs', exist_ok=True)
    log['last_run'] = datetime.now().isoformat()
    with open(LOG_FILE, 'w') as f:
        json.dump(log, f, indent=2)

def should_engage(submission, log):
    """Determine if we should engage with this post"""
    # Already commented?
    if submission.id in log['commented_posts']:
        return False, None
    
    # Too old? (only engage with posts from last 24 hours)
    post_time = datetime.fromtimestamp(submission.created_utc)
    if datetime.now() - post_time > timedelta(hours=24):
        return False, None
    
    # Check for keywords in title/body
    text = f"{submission.title} {submission.selftext}".lower()
    
    # Determine response type
    if any(kw in text for kw in ['lake level', 'water level', 'lake', 'dam']):
        return True, 'lake_level'
    elif any(kw in text for kw in ['fishing', 'fish', 'bass', 'cod']):
        return True, 'fishing'
    elif any(kw in text for kw in ['scriptable', 'widget', 'ios']):
        return True, 'scriptable'
    
    return False, None

def get_response(response_type, link):
    """Get a varied response"""
    import random
    template = random.choice(RESPONSES[response_type])
    return template.format(link=link)

def main():
    print(f"🤖 Reddit Monitor starting at {datetime.now()}")
    
    # Load credentials
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        username=os.getenv('REDDIT_USERNAME'),
        password=os.getenv('REDDIT_PASSWORD'),
        user_agent='VicLakesWidget/1.0'
    )
    
    gumroad_link = os.getenv('GUMROAD_LINK', 'https://dgtlgav.gumroad.com')
    
    # Load activity log
    log = load_activity_log()
    print(f"📋 Loaded log: {len(log['commented_posts'])} previous engagements")
    
    engagement_count = 0
    max_engagements = 3  # Max 3 comments per run to avoid spam
    
    # Monitor subreddits
    for subreddit_name in SUBREDDITS:
        if engagement_count >= max_engagements:
            print(f"⚠️ Hit max engagements ({max_engagements}), stopping")
            break
            
        print(f"\n🔍 Checking r/{subreddit_name}...")
        subreddit = reddit.subreddit(subreddit_name)
        
        try:
            # Check new and hot posts
            for submission in subreddit.new(limit=25):
                should_comment, response_type = should_engage(submission, log)
                
                if should_comment and engagement_count < max_engagements:
                    print(f"\n✅ Found relevant post: {submission.title[:60]}...")
                    print(f"   Type: {response_type}")
                    print(f"   URL: https://reddit.com{submission.permalink}")
                    
                    # Get response
                    response = get_response(response_type, gumroad_link)
                    
                    # Comment - LIVE MODE
                    try:
                        submission.reply(response)
                        print(f"   ✅ Commented successfully!")
                    except Exception as e:
                        print(f"   ❌ Failed to comment: {e}")
                        continue
                    
                    # Log the engagement
                    log['commented_posts'].append(submission.id)
                    engagement_count += 1
                    
                    # Be polite - wait between comments
                    time.sleep(30)
                    
        except Exception as e:
            print(f"❌ Error in r/{subreddit_name}: {e}")
            continue
    
    # Save activity log
    save_activity_log(log)
    print(f"\n✅ Monitor complete. Engaged with {engagement_count} posts")
    print(f"📊 Total historical engagements: {len(log['commented_posts'])}")

if __name__ == '__main__':
    main()
