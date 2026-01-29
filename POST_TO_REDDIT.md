# How to Post to Reddit

## Quick Start (Automated)

### Step 1: Get Reddit Credentials
1. Go to https://www.reddit.com/prefs/apps
2. Click "create another app..."
3. Fill in:
   - Name: `Victoria Lakes Widget`
   - App type: Select **"script"**
   - Redirect URI: `http://localhost:8080`
4. Click "create app"
5. Copy your `CLIENT_ID` (under the app name) and `CLIENT_SECRET`

### Step 2: Set Up Environment
```bash
cd victoria-lakes-automation

# Create .env file with your credentials
cat > .env << EOF
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
GUMROAD_LINK=https://dgtlgav.gumroad.com
EOF

# Install dependencies
pip3 install praw python-dotenv
```

### Step 3: Post!
```bash
python3 scripts/reddit_post.py
```

This will post to:
- ✅ r/Scriptable
- ✅ r/iOSsetups
- ✅ r/melbourne

**Note:** Wait 24-48 hours between posts to avoid spam detection.

---

## Manual Posting (No Setup Required)

### r/Scriptable
1. Go to: https://reddit.com/r/Scriptable/submit
2. Title: `I made a Victorian lakes water level widget for Scriptable (22 lakes supported)`
3. Upload video: `/Users/gav/Documents/Example Workspace/victoria-lakes-automation/demo-video.mp4`
4. Body: (Copy from REDDIT_POST.md)
5. Click "Post"

### r/melbourne  
1. Go to: https://reddit.com/r/melbourne/submit
2. Title: `Made an iPhone widget for Victorian lake levels (Eildon, Mulwala, Nagambie, etc.)`
3. Upload video
4. Body: (Copy from REDDIT_POST.md)
5. Post!

---

## Posting Schedule

**Day 1:** r/Scriptable (tech-focused audience)
**Day 3:** r/iOSsetups (design-focused)
**Day 5:** r/melbourne (local audience)
**Day 7:** r/AusFishing (fishing-focused)
**Day 9:** r/boating (boating-focused)

Spread them out to avoid spam detection and max out reach.

---

## What to Expect

**r/Scriptable:**
- High engagement from widget enthusiasts
- Expect questions about code/setup
- 50-200 upvotes typical

**r/melbourne:**
- Local relevance = good engagement
- Potential for viral growth (200-500+ upvotes possible)
- Real users = real sales

**r/iOSsetups:**
- Design-focused feedback
- Screenshot requests
- 20-100 upvotes

---

Ready to post?
