# Instagram-Brave-Bot
This is a Instagram unfollow/follow bot which uses Selenium to automate its functions, with the Brave Browser.

# Instructions
1. The script will first need dependencies.
So first, open up your command prompt and type:
- pip install browser
- pip install selenium
- pip install time
- pip install password

2. After that, you will have to change the driver path with your own.
To install the driver, go to https://chromedriver.chromium.org/downloads and pick the version that matches your Brave Browser.  You will also have to change the Brave path, you can install Brave here: https://brave.com/

3. Change the send keys input to your email and password, this is safe as long as you don't open the file infront of people or send it to your friends.

4. At the bottom, uncomment either Follow() or Unfollow() depending on what you want to use.

5. Run the script as brave.py and Selenium should open the browser for you.

# Why did you make this?

I saw someone make a Chrome-version of this, however the entire process was bad. It stopped functioning the moment it encountered no follow buttons on the page. I also tried first to make Selenium scroll down bit by bit, but to make it easier, it would refresh after every tenth follow. One extra addition I made is that if you open a new browser with the bot-software, it will request you to accept cookies, and this also implemented it. Be warned however, Instagram knows this and they have put in procedures which block you from following or unfollowing anyone for 15 minutes if you abuse it. You do not get any other account restrictions though.

If you encounter any problems, try extending the sleep timer for the script. It might happen due to your internet loading too slow, and then Selenium can't catch up, or Instagram has updated the site and the script is broken.

Have fun.
