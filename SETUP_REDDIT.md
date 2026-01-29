# Reddit Bot Setup - Get API Credentials

## Step 1: Create a Reddit App

1. **Go to:** https://www.reddit.com/prefs/apps
2. **Log in** with your Reddit account (create one if you don't have it)
3. **Scroll to the bottom** and click **"create another app..."**

## Step 2: Fill in the App Details

- **Name:** `Victoria Lakes Bot` (or any name)
- **App type:** Select **"script"** (radio button)
- **Description:** `Automated bot for lake-related communities`
- **About URL:** Leave blank
- **Redirect URI:** `http://localhost:8080`
- **Click:** "create app"

## Step 3: Get Your Credentials

After creating the app, you'll see:

```
personal use script
[THIS IS YOUR CLIENT_ID - copy this]

secret
[THIS IS YOUR CLIENT_SECRET - copy this]
```

**Copy these two values!**

## Step 4: Add Secrets to GitHub

1. Go to: https://github.com/GavinWhitfort/victoria-lakes-marketing/settings/secrets/actions

2. Click **"New repository secret"** for each of these:

**Secret #1:**
- Name: `REDDIT_CLIENT_ID`
- Value: [paste the CLIENT_ID from step 3]

**Secret #2:**
- Name: `REDDIT_CLIENT_SECRET`
- Value: [paste the CLIENT_SECRET from step 3]

**Secret #3:**
- Name: `REDDIT_USERNAME`
- Value: [your Reddit username]

**Secret #4:**
- Name: `REDDIT_PASSWORD`
- Value: [your Reddit password]

**Secret #5:**
- Name: `GUMROAD_LINK`
- Value: `https://dgtlgav.gumroad.com`

## Step 5: Test the Bot Locally (Optional)

```bash
cd victoria-lakes-automation

# Install dependencies
pip3 install -r requirements.txt

# Create .env file
cat > .env << 'EOF'
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USERNAME=your_username_here
REDDIT_PASSWORD=your_password_here
GUMROAD_LINK=https://dgtlgav.gumroad.com
EOF

# Run the bot
python3 scripts/reddit_monitor.py
```

## Step 6: Activate GitHub Actions

Once secrets are added, the bot will run automatically every 6 hours.

**To trigger it manually:**
1. Go to: https://github.com/GavinWhitfort/victoria-lakes-marketing/actions
2. Click **"Reddit Lake Monitor"**
3. Click **"Run workflow"** → **"Run workflow"**

## 🎉 You're Live!

The bot will now:
- Run every 6 hours automatically
- Monitor 9 subreddits for lake-related posts
- Comment authentically (max 3 per run)
- Log all activity to avoid duplicates

## 📊 Monitor Results

Check the bot's activity:
- **Logs:** https://github.com/GavinWhitfort/victoria-lakes-marketing/actions
- **Comments:** Check your Reddit account's comment history

## ⚠️ Safety Notes

- Bot is already rate-limited (max 3 comments per 6 hours)
- Responses are varied and natural
- If you get downvoted or banned, dial back the frequency
- You can pause anytime by disabling the GitHub Action

---

**Need help?** The bot is live and ready to go once you add the secrets!
