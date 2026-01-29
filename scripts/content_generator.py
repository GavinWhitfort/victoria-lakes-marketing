#!/usr/bin/env python3
"""
Social Media Content Generator for Victoria Lakes Widget
Generates ready-to-post content for TikTok, Instagram, Twitter, etc.
"""

import json
import random
from datetime import datetime
import os

# Lake data for content variations
POPULAR_LAKES = [
    'Lake Eildon', 'Lake Mulwala', 'Lake Nagambie', 
    'Lake Buffalo', 'Dartmouth Dam', 'Lake Hume',
    'Lake Eppalock', 'Yarrawonga Weir'
]

ACTIVITIES = [
    'boating', 'fishing', 'jet skiing', 'wake boarding',
    'camping', 'water skiing', 'kayaking'
]

# Content templates for different platforms

TIKTOK_HOOKS = [
    "POV: You check the lake level before packing the boat 😎",
    "This iPhone widget changed my fishing game forever",
    "Stop opening 5 websites to check water levels",
    "Me: checks lake website\nAlso me: *confused*\nSolution:",
    "Victorian fishers/boaters - you need this",
    "The lake level hack nobody told you about",
    "When the lake is down and you drove 2 hours... 💀",
    "How to never waste a trip to the lake again",
    "This is how I check lake levels now (game changer)",
    "Before vs After using this widget"
]

INSTAGRAM_CAPTIONS = [
    "🌊 Never guess lake levels again.\n\nBuilt this widget for all the Victorian boaters, fishers, and campers who are sick of checking clunky government websites.\n\n✅ 22+ lakes (Eildon, Mulwala, Nagambie, Buffalo...)\n✅ Live water levels + weekly trends\n✅ Right on your iPhone home screen\n\nLink in bio 🔗\n\n#VictorianLakes #LakeEildon #BoatingVictoria #FishingAustralia #iOSWidgets #Scriptable",
    
    "📊 Lake Eildon sitting at 87% this week ↗️\n\nTracking water levels just got way easier. This Scriptable widget shows real-time data for 22 Victorian lakes - perfect for planning your next boat trip or fishing session.\n\nSwipe to see the setup 👉\n\n#LakeEildon #VictorianFishing #BoatingLife #iOSWidgets",
    
    "🎣 Fish movement = water movement\n\nThat's why I built this widget. Track weekly rises and falls for Lake Eildon, Mulwala, Nagambie + 19 more Victorian lakes.\n\nKnow the conditions before you leave home.\n\nLink in bio.\n\n#FishingVictoria #BassFishing #LakeFishing #TechForAnglers"
]

TWITTER_POSTS = [
    "Built a free Scriptable widget for Victorian lake levels 🌊\n\n22 lakes supported (Eildon, Mulwala, Nagambie...)\nLive data + weekly trends\niPhone home screen\n\nPerfect for boaters/fishers/campers\n\n{link}\n\n#VictorianLakes #BoatingVic",
    
    "Tired of checking lake websites?\n\nMade a widget: Lake Eildon, Hume, Mulwala, Buffalo, Nagambie + 17 more\n\nLive water levels on your iPhone. Weekly change indicators.\n\n{link}\n\n#FishingAustralia #LakeEildon",
    
    "Lake Eildon: 87% full ↑ (+2% this week)\n\nGet this data on your iPhone home screen with our Scriptable widget. 22 Victorian lakes supported.\n\n{link}\n\n#LakeEildon #VictorianBoating"
]

REDDIT_POST_TITLES = [
    "I built a Scriptable widget for Victorian lake water levels (Eildon, Mulwala, Nagambie, etc.)",
    "Fellow Victorian boaters/fishers - made this widget to track lake levels",
    "[iOS] Real-time water level widget for 22 Victorian lakes",
    "Stop checking clunky government sites - I made a lake levels widget",
    "Victorian lakes widget for Scriptable (feedback welcome)"
]

REDDIT_POST_BODIES = [
    """Got sick of checking multiple government websites before heading to Lake Eildon, so I built a Scriptable widget that shows:

• Live water levels (% full)
• Weekly change indicators (rising/falling)
• Total volume in megalitres
• Support for 22 Victorian lakes

Works on iPhone, iPad, and Mac. Three widget sizes available.

Perfect for boaters, fishers, and campers who want to know conditions before the trip.

Lakes supported: Eildon, Hume, Mulwala, Nagambie, Buffalo, Dartmouth, Eppalock, and more.

{link}

Feedback welcome! What other features would be useful?""",

    """Victorian boaters/fishers - built this for us.

I was tired of:
- Opening 5 different websites to check lake levels
- Guessing if the water was high enough
- Driving 2 hours only to find low water

So I built a Scriptable widget that solves all of this.

**Features:**
- Real-time data for 22 Victorian lakes
- Weekly trends (is it rising or falling?)
- Glanceable on your home screen
- Small, medium, and large widgets

**Supported lakes:** Eildon, Mulwala, Nagambie, Buffalo, Hume, Dartmouth, Eppalock, Yarrawonga, and more.

{link}

Let me know what you think!"""
]

FACEBOOK_POSTS = [
    """🌊 Victorian boaters, fishers, campers - this one's for you!

Just launched a new iPhone widget that shows LIVE water levels for 22 Victorian lakes.

✅ Lake Eildon
✅ Lake Mulwala  
✅ Lake Nagambie
✅ Lake Buffalo
✅ Dartmouth Dam
... and 17 more!

Never guess lake conditions again. Weekly trends show if it's rising or falling.

Perfect for planning your weekend trips 🚤🎣🏕️

Check it out: {link}""",

    """Who else checks lake levels before heading out? 🙋‍♂️

I got sick of opening clunky websites, so I built an iPhone widget that shows:
• Live water levels
• Weekly change indicators  
• 22 Victorian lakes

Eildon | Mulwala | Nagambie | Buffalo | Hume | Eppalock | and more

Link: {link}

Game changer for planning boating and fishing trips!"""
]

def generate_tiktok_scripts(count=20):
    """Generate TikTok/Reels scripts"""
    scripts = []
    
    for i in range(count):
        hook = random.choice(TIKTOK_HOOKS)
        lake = random.choice(POPULAR_LAKES)
        activity = random.choice(ACTIVITIES)
        
        script = f"""**TikTok Script #{i+1}**
        
Hook: {hook}

Visual: Screen recording showing:
1. Opening phone
2. Widget showing {lake} at X% full
3. Quick swipe to show other lakes
4. Zoom in on weekly trend indicator

Text overlay: "22 Victorian lakes • Live data • Free setup"

CTA: "Link in bio for setup guide"

Hashtags: #FishingAustralia #VictorianLakes #iOSWidgets #Scriptable #BoatingLife #LakeEildon #{activity.replace(' ', '')}

Duration: 30-45 seconds
Music: Trending upbeat track
"""
        scripts.append(script)
    
    return scripts

def generate_instagram_posts(count=15):
    """Generate Instagram carousel/post content"""
    posts = []
    
    for i in range(count):
        caption = random.choice(INSTAGRAM_CAPTIONS)
        lake = random.choice(POPULAR_LAKES)
        
        post = f"""**Instagram Post #{i+1}**

Caption:
{caption}

Image ideas:
- Slide 1: Widget screenshot on iPhone home screen
- Slide 2: Close-up of {lake} widget showing live data
- Slide 3: Setup instructions (numbered steps)
- Slide 4: All supported lakes list
- Slide 5: Before/After (website vs widget)

Format: Carousel (5 slides)
Aspect ratio: 1:1 (square)

CTA: "Link in bio 🔗"
"""
        posts.append(post)
    
    return posts

def generate_twitter_posts(count=20, link='https://dgtlgav.gumroad.com'):
    """Generate Twitter/X posts"""
    posts = []
    
    for i in range(count):
        post = random.choice(TWITTER_POSTS).format(link=link)
        posts.append(f"**Tweet #{i+1}**\n\n{post}\n")
    
    return posts

def generate_reddit_posts(count=10, link='https://dgtlgav.gumroad.com'):
    """Generate Reddit post content"""
    posts = []
    
    for i in range(count):
        title = random.choice(REDDIT_POST_TITLES)
        body = random.choice(REDDIT_POST_BODIES).format(link=link)
        
        post = f"""**Reddit Post #{i+1}**

Title: {title}

Body:
{body}

Suggested subreddits:
- r/Scriptable
- r/iOSsetups  
- r/melbourne
- r/AusFishing
- r/boating

Post as: Authentic user sharing their creation
Tone: Helpful, not salesy
"""
        posts.append(post)
    
    return posts

def generate_facebook_posts(count=10, link='https://dgtlgav.gumroad.com'):
    """Generate Facebook group posts"""
    posts = []
    
    for i in range(count):
        post_text = random.choice(FACEBOOK_POSTS).format(link=link)
        
        post = f"""**Facebook Post #{i+1}**

{post_text}

Image: Widget screenshot showing multiple lakes

Suggested groups:
- Boating Victoria
- Fishing Victoria  
- Lake Eildon Community
- Murray River Boating
- Caravan & Camping Australia

Tone: Friendly, community-focused
"""
        posts.append(post)
    
    return posts

def save_content(content_dict):
    """Save all content to organized files"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = f'content/{timestamp}'
    os.makedirs(output_dir, exist_ok=True)
    
    for platform, content_list in content_dict.items():
        filepath = f'{output_dir}/{platform}.txt'
        with open(filepath, 'w') as f:
            f.write(f"=== {platform.upper()} CONTENT ===\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write('\n\n---\n\n'.join(content_list))
        print(f"✅ Saved {len(content_list)} {platform} posts to {filepath}")
    
    # Also save a master JSON
    json_path = f'{output_dir}/content.json'
    with open(json_path, 'w') as f:
        json.dump(content_dict, f, indent=2)
    print(f"✅ Saved JSON to {json_path}")

def main():
    print("🎨 Generating social media content...\n")
    
    link = 'https://dgtlgav.gumroad.com'
    
    content = {
        'tiktok_reels': generate_tiktok_scripts(20),
        'instagram': generate_instagram_posts(15),
        'twitter': generate_twitter_posts(20, link),
        'reddit': generate_reddit_posts(10, link),
        'facebook': generate_facebook_posts(10, link)
    }
    
    save_content(content)
    
    print("\n✅ Content generation complete!")
    print("\nSummary:")
    for platform, posts in content.items():
        print(f"  - {platform}: {len(posts)} posts")

if __name__ == '__main__':
    main()
