#!/usr/bin/env python3
"""
Reddit Auto-Poster for Victoria Lakes Widget
Posts to multiple subreddits with video
"""

import praw
import os
from dotenv import load_dotenv

load_dotenv()

# Reddit credentials (set in .env file)
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    username=os.getenv('REDDIT_USERNAME'),
    password=os.getenv('REDDIT_PASSWORD'),
    user_agent='VicLakesWidget/1.0'
)

VIDEO_PATH = '/Users/gav/Documents/Example Workspace/victoria-lakes-automation/demo-video.mp4'

# Post configurations
POSTS = {
    'Scriptable': {
        'title': 'I made a Victorian lakes water level widget for Scriptable (22 lakes supported)',
        'body': """Hey everyone! Built a Scriptable widget for Victorian lake water levels that I thought might be useful for other boaters/fishers/campers.

**Features:**
- Live water levels for 22 Victorian lakes
- Weekly change indicators (rising/falling %)
- Three sizes (small, medium, large)
- Clean visual design with wave patterns
- Total volume in megalitres

**Supported lakes:** Eildon, Hume, Mulwala, Nagambie, Buffalo, Dartmouth, Eppalock, Yarrawonga, and more.

I got sick of checking clunky government websites before heading out, so I built this. Glanceable data right on the home screen.

Available here: https://dgtlgav.gumroad.com

Let me know if you have feedback or feature requests!"""
    },
    
    'iOSsetups': {
        'title': 'Victorian Lakes Widget - Clean data display for Scriptable',
        'body': """Built a custom Scriptable widget for Victorian lake water levels. Went for a clean, glanceable design with big numbers and visual wave patterns.

**Design details:**
- Aqua blue theme matches the water vibe
- Large typography for quick reading
- Week change shown in red/green
- Wave pattern indicates water level visually
- Small, medium, large sizes available

Supports 22 Victorian lakes including Eildon, Mulwala, Nagambie, Buffalo, etc.

Link: https://dgtlgav.gumroad.com

Feedback welcome!"""
    },
    
    'melbourne': {
        'title': 'Made an iPhone widget for Victorian lake levels (Eildon, Mulwala, Nagambie, etc.)',
        'body': """Fellow Victorian boaters/fishers - built this for us.

I was tired of:
- Opening 5 different government websites to check lake levels
- Guessing if the water was high enough
- Driving 2 hours to Eildon only to find disappointing water

So I made a Scriptable widget that shows live levels + weekly trends for 22 Victorian lakes.

Works on iPhone, iPad, Mac. Small, medium, and large widgets.

**Lakes supported:** Eildon, Hume, Mulwala, Nagambie, Buffalo, Dartmouth, Eppalock, Yarrawonga, Goulburn Weir, Lake Charm, Tullaroop, and more.

Check it out: https://dgtlgav.gumroad.com

Let me know what you think or if there's other lakes you'd want added!"""
    }
}

def post_to_subreddit(subreddit_name, title, body, video_path):
    """Post to a subreddit with video"""
    try:
        subreddit = reddit.subreddit(subreddit_name)
        
        # Upload video and create post
        submission = subreddit.submit_video(
            title=title,
            video_path=video_path,
            selftext=body
        )
        
        print(f"✅ Posted to r/{subreddit_name}: {submission.url}")
        return submission
        
    except Exception as e:
        print(f"❌ Failed to post to r/{subreddit_name}: {e}")
        return None

def main():
    print("🚀 Starting Reddit auto-poster...\n")
    
    # Check if video exists
    if not os.path.exists(VIDEO_PATH):
        print(f"❌ Video not found: {VIDEO_PATH}")
        return
    
    print(f"📹 Video found: {VIDEO_PATH}\n")
    
    # Post to each subreddit
    results = {}
    for subreddit, config in POSTS.items():
        print(f"📤 Posting to r/{subreddit}...")
        submission = post_to_subreddit(
            subreddit,
            config['title'],
            config['body'],
            VIDEO_PATH
        )
        results[subreddit] = submission
        print()
    
    # Summary
    print("\n📊 Summary:")
    for subreddit, submission in results.items():
        if submission:
            print(f"  ✅ r/{subreddit}: {submission.url}")
        else:
            print(f"  ❌ r/{subreddit}: Failed")

if __name__ == '__main__':
    main()
