# Reddit Pain Point Scanner

**Automatically discover product opportunities by scanning Reddit for pain points.**

## What It Does

Monitors 30+ subreddits daily for:
- "I wish there was..."
- "Why doesn't X exist?"
- "Is there an app for..."
- "I hate that..."
- "Someone needs to make..."

Then generates a daily report with:
- 🔥 Top pain points (by engagement)
- 📊 Categorized by type (mobile app, web tool, automation, etc.)
- 🔗 Links to discussions
- 💬 Engagement metrics (upvotes, comments)

## How It Works

1. **Scans 30+ subreddits** every 24 hours
2. **Pattern matching** finds complaints and wishes
3. **Categorizes** by product type (app, web, automation, etc.)
4. **Ranks** by engagement (upvotes/comments)
5. **Generates report** in markdown

## Subreddits Monitored

**Entrepreneurship:**
- r/Entrepreneur, r/SaaS, r/startups, r/indiehackers, r/SideProject

**Tech & Productivity:**
- r/iOS, r/iphone, r/androidapps, r/productivity, r/webdev

**Australian:**
- r/australia, r/melbourne, r/AusFinance, r/AusFishing, r/boating

**Niches:**
- r/camping, r/Fishing, r/personalfinance, r/LifeProTips

## Setup

### Step 1: Reddit Credentials
Same as the Reddit monitor bot - use your existing credentials.

### Step 2: Run Locally (Test)

```bash
cd victoria-lakes-automation

# Install dependencies
pip3 install praw python-dotenv

# Run scanner
python3 scripts/reddit_pain_point_scanner.py
```

**Output:**
- `pain_points/report_YYYY-MM-DD.md` - Daily report
- `pain_points/daily_report.md` - Latest report
- `pain_points/daily_log.json` - Raw data

### Step 3: Automate (GitHub Actions)

Once Reddit secrets are added to GitHub (same ones from monitor bot), this runs automatically **every day at 9 AM**.

Manual trigger:
1. Go to: https://github.com/GavinWhitfort/victoria-lakes-marketing/actions
2. Select "Reddit Pain Point Scanner"
3. Click "Run workflow"

## Example Output

```markdown
# Reddit Pain Points Report
**Date:** 2026-01-29
**Total Pain Points Found:** 47

## 🔥 Hot Pain Points (High Engagement)

### 1. I wish there was an app to track water levels for lakes
- **Subreddit:** r/boating
- **Score:** 234 upvotes | 56 comments
- **Category:** mobile_app, data_tracking
- **URL:** https://reddit.com/r/boating/...

**Excerpt:**
> Always checking websites before heading out. Someone needs to make
> a simple app that just shows if the lake has enough water...

---

### 2. Why isn't there a tool to automate invoice reminders?
- **Subreddit:** r/smallbusiness
- **Score:** 189 upvotes | 34 comments
- **Category:** automation, finance
- **URL:** https://reddit.com/r/smallbusiness/...
```

## Use Cases

**Find your next product:**
- Scan for repeated pain points
- Identify gaps in existing tools
- Validate demand (high engagement = high demand)

**Niche discovery:**
- Australian-specific problems
- Local market opportunities
- Regional pain points

**Market research:**
- See what people actually complain about
- Understand real-world problems
- Find underserved niches

## Categories

Pain points are auto-categorized:
- **mobile_app** - iOS/Android app ideas
- **web_tool** - Web-based tools/SaaS
- **automation** - Workflow automation
- **data_tracking** - Monitoring/tracking tools
- **productivity** - Organization/planning
- **finance** - Money/budgeting tools
- **local_services** - Location-based services

## Schedule

**Default:** Daily at 9 AM AEST

**Customizable:** Edit `.github/workflows/pain-point-scanner.yml` cron schedule

## Tips

1. **Read the reports weekly** - Patterns emerge over time
2. **Look for repeated themes** - Same pain point = validated demand
3. **Check engagement** - High upvotes = people care
4. **Focus on Australian posts** - Local opportunity
5. **Build what you see 3+ times** - Validation threshold

## Next Steps

1. Run scanner today: `python3 scripts/reddit_pain_point_scanner.py`
2. Check report: `pain_points/daily_report.md`
3. Add Reddit secrets to GitHub for automation
4. Get daily pain points delivered automatically

---

**Your personal product idea machine. 🚀**
