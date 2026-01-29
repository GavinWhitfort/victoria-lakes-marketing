#!/usr/bin/env python3
"""
Reddit Auto-Poster V2 - Link-Friendly Subreddits
Posts to communities that welcome product showcases
"""

import praw
import os
from dotenv import load_dotenv
import time

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    username=os.getenv('REDDIT_USERNAME'),
    password=os.getenv('REDDIT_PASSWORD'),
    user_agent='VicLakesWidget/1.0'
)

VIDEO_PATH = '/Users/gav/Documents/Example Workspace/victoria-lakes-automation/demo-video.mp4'
LINK = 'https://dgtlgav.gumroad.com'

# Link-friendly subreddits that welcome product posts
POSTS = {
    'SideProject': {
        'title': 'Built an iPhone widget for Victorian lake water levels (22 lakes supported)',
        'body': f"""Hey everyone! Just launched a Scriptable widget for Victorian lake water levels.

**What it does:**
- Shows live water levels for 22 Victorian lakes
- Weekly change indicators (rising/falling %)
- Three widget sizes (small, medium, large)
- Clean visual design with wave patterns

**Why I built it:**
Got tired of checking multiple government websites before boating/fishing trips. Wanted glanceable data right on my home screen.

**Supported lakes:** Eildon, Hume, Mulwala, Nagambie, Buffalo, Dartmouth, Eppalock, Yarrawonga, and 14 more.

[Video showing the widgets in action]

Check it out: {LINK}

Would love feedback from the community! What features would make this more useful?

**Tech:** Built with Scriptable (iOS), pulls data from Victorian water authorities API.
"""
    },
    
    'somethingimade': {
        'title': 'I made an iPhone widget that shows Victorian lake water levels',
        'body': f"""Built a widget for checking lake levels before heading out boating/fishing!

Shows live data for 22 Victorian lakes including Eildon, Mulwala, Nagambie, Buffalo, etc.

[Video attached showing three widget sizes]

**Features:**
- Real-time water level percentages
- Weekly rise/fall indicators
- Volume in megalitres
- Clean blue wave design

Previously I'd have to open 5 different websites to check conditions. Now it's right on my home screen.

Link: {LINK}

Happy to answer any questions about how I built it!
"""
    },
    
    'indiehackers': {
        'title': 'Launched: Victorian Lakes Widget for iPhone - $5-7 MRR so far',
        'body': f"""**Product:** iPhone widget showing live water levels for 22 Victorian lakes

**Problem:** Boaters/fishers/campers waste time checking multiple government websites for lake conditions before trips

**Solution:** Scriptable widget with glanceable data on iPhone home screen

**Tech:** JavaScript (Scriptable app), Victorian water authority APIs, real-time data

**Pricing:** $5 single color, $7 bundle (3 colors)

**Launch:** Soft launched on Gumroad 2 weeks ago

**Results so far:**
- 1 sale (just getting started!)
- Building automated marketing (Reddit bot, social content generator)

[Video showing the widget in action]

**Next steps:**
- Reddit automation for organic reach
- TikTok/Instagram content push
- SEO landing pages for each lake

Link: {LINK}

**Question for the community:** What marketing channels have worked for niche iOS products like this?
"""
    }
}

def post_to_subreddit(subreddit_name, title, body, video_path=None, url=None):
    """Post to a subreddit"""
    try:
        subreddit = reddit.subreddit(subreddit_name)
        
        if video_path and os.path.exists(video_path):
            # Video post
            submission = subreddit.submit_video(
                title=title,
                video_path=video_path,
                selftext=body
            )
        elif url:
            # Link post
            submission = subreddit.submit(
                title=title,
                url=url,
                selftext=body
            )
        else:
            # Text post
            submission = subreddit.submit(
                title=title,
                selftext=body
            )
        
        print(f"✅ Posted to r/{subreddit_name}:")
        print(f"   {submission.url}\n")
        return submission
        
    except Exception as e:
        print(f"❌ Failed to post to r/{subreddit_name}:")
        print(f"   {e}\n")
        return None

def main():
    print("🚀 Reddit Auto-Poster V2 (Link-Friendly Subreddits)\n")
    print("=" * 60)
    
    if not os.path.exists(VIDEO_PATH):
        print(f"⚠️  Video not found: {VIDEO_PATH}")
        print("Posting without video...\n")
        video_path = None
    else:
        print(f"✅ Video found: {VIDEO_PATH}\n")
        video_path = VIDEO_PATH
    
    results = {}
    
    for i, (subreddit, config) in enumerate(POSTS.items(), 1):
        print(f"[{i}/{len(POSTS)}] Posting to r/{subreddit}...")
        print("-" * 60)
        
        submission = post_to_subreddit(
            subreddit,
            config['title'],
            config['body'],
            video_path=video_path
        )
        
        results[subreddit] = submission
        
        # Wait between posts to avoid rate limiting
        if i < len(POSTS):
            print("⏳ Waiting 60 seconds before next post...\n")
            time.sleep(60)
    
    print("=" * 60)
    print("\n📊 POSTING SUMMARY\n")
    
    for subreddit, submission in results.items():
        if submission:
            print(f"✅ r/{subreddit}")
            print(f"   {submission.url}")
        else:
            print(f"❌ r/{subreddit} - Failed")
        print()
    
    print("Done! Check Reddit for engagement.")

if __name__ == '__main__':
    main()
