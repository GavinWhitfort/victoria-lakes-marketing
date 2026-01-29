# Victoria Lakes Widget - Marketing Automation

Automated marketing tools for the Victoria Lakes Scriptable widget product.

## 🤖 Automation Tools

### 1. Reddit Monitor Bot (`scripts/reddit_monitor.py`)
Monitors Victorian subreddits for lake-related posts and engages authentically.

**Features:**
- Monitors 9 subreddits (r/melbourne, r/AusFishing, r/boating, etc.)
- Keyword detection for lake/fishing/widget posts
- Varied, natural-sounding responses
- Rate limiting (max 3 comments per run)
- Activity logging to avoid duplicate comments

**Setup:**
1. Create a Reddit app at https://www.reddit.com/prefs/apps
2. Add secrets to GitHub repo:
   - `REDDIT_CLIENT_ID`
   - `REDDIT_CLIENT_SECRET`  
   - `REDDIT_USERNAME`
   - `REDDIT_PASSWORD`
   - `GUMROAD_LINK`

3. Enable GitHub Actions in your repo

**Testing locally:**
```bash
cd victoria-lakes-automation
pip install praw python-dotenv

# Create .env file:
echo "REDDIT_CLIENT_ID=your_id" > .env
echo "REDDIT_CLIENT_SECRET=your_secret" >> .env
echo "REDDIT_USERNAME=your_username" >> .env
echo "REDDIT_PASSWORD=your_password" >> .env
echo "GUMROAD_LINK=https://dgtlgav.gumroad.com" >> .env

# Run (will only log, won't actually comment until you uncomment line 137)
python scripts/reddit_monitor.py
```

**Go Live:**
- Uncomment line 137 in `reddit_monitor.py`: `submission.reply(response)`
- Push to GitHub - runs every 6 hours automatically

---

### 2. Content Generator (`scripts/content_generator.py`)
Generates ready-to-post content for all platforms.

**Output:**
- 20 TikTok/Reels scripts with hooks and shot lists
- 15 Instagram carousel posts with captions
- 20 Twitter/X posts
- 10 Reddit posts with titles and bodies
- 10 Facebook group posts

**Usage:**
```bash
cd victoria-lakes-automation
python scripts/content_generator.py
```

**Output location:** `content/YYYYMMDD_HHMMSS/`

**What you get:**
- `tiktok_reels.txt` - 20 video scripts with hooks, visuals, CTAs
- `instagram.txt` - 15 carousel post ideas with captions
- `twitter.txt` - 20 ready-to-tweet posts
- `reddit.txt` - 10 Reddit posts with suggested subreddits
- `facebook.txt` - 10 Facebook group posts
- `content.json` - All content in JSON format for automation

---

## 📅 Recommended Schedule

### Week 1: Setup
- [ ] Set up Reddit bot with secrets
- [ ] Generate initial content batch (run content generator)
- [ ] Test Reddit bot locally
- [ ] Create social media accounts if needed (@VicLakeLevels on Twitter?)

### Week 2: Manual Posting
- [ ] Post 1-2 TikTok/Reels per day from generated content
- [ ] Post to Instagram 3x per week
- [ ] Tweet daily using generated posts
- [ ] Post to 1 Reddit community (test response)

### Week 3: Enable Automation
- [ ] Enable Reddit bot (uncomment reply line, push to GitHub)
- [ ] Set up Buffer/Later for scheduled social posts
- [ ] Monitor results and engagement

### Week 4: Optimize
- [ ] Review what's working (which platforms, content types)
- [ ] Generate new content batch with learnings
- [ ] Add more subreddits if Reddit bot is successful

---

## 🎯 Next Steps

1. **Create GitHub repo** for this project
2. **Set up Reddit app** and get credentials
3. **Run content generator** to get your first 75+ posts
4. **Test Reddit bot locally** before going live
5. **Schedule first week of content** using generated posts

---

## 📊 Tracking

Monitor these metrics:
- Gumroad sales (direct attribution)
- Reddit comment upvotes/replies (engagement quality)
- Social media link clicks (use UTM parameters)
- Subreddit bans (if bot is too aggressive, dial back)

---

## ⚠️ Important Notes

**Reddit Bot:**
- Currently in "dry run" mode (logs but doesn't comment)
- Uncomment line 137 to enable actual commenting
- Start with 1-2 comments per day, increase gradually
- Be authentic - these are real communities
- Monitor for negative feedback and adjust

**Content Generator:**
- Review generated content before posting
- Customize with your brand voice
- Add real screenshots/photos for visuals
- Update lake percentages with real data periodically

---

## 🚀 Quick Start

```bash
# Generate 75+ ready-to-post pieces of content
cd victoria-lakes-automation
python scripts/content_generator.py

# Check the output
open content/

# Set up Reddit monitoring (requires GitHub secrets)
# See setup instructions above
```

---

Built with ❤️ for Victorian boaters, fishers, and campers.
