# Instagram-Brave-Bot
This is a Instagram unfollow/follow bot which uses Selenium to automate its functions, with the Brave Browser.

# Instructions
1. The script will first need dependencies, so navigate to the Instagram-Brave-Bot directory and type "pip install -r requirements.txt"

2. Usage: 
python brave.py --follow
python brave.py --unfollow

3. Finally, enter your driver path and brave path.
- https://chromedriver.chromium.org/downloads
- https://brave.com/

# Why did you make this?
I saw someone make a Chrome-version of this, however the entire process was bad. It stopped functioning the moment it encountered no follow buttons on the page. I also tried first to make Selenium scroll down bit by bit, but to make it easier, it would refresh after every tenth follow. One extra addition I made is that if you open a new browser with the bot-software, it will request you to accept cookies, and this also implemented it. Be warned however, Instagram knows this and they have put in procedures which block you from following or unfollowing anyone for 15 minutes if you abuse it. You do not get any other account restrictions though.

If you encounter any problems, try extending the sleep timer for the script. It might happen due to your internet loading too slow, and then Selenium can't catch up, or Instagram has updated the site and the script is broken.

Have fun.
