# CIS-024-Final
# Yosemite Campsite Scraper
\
Have you ever wanted to go camping at Yosemite, but hated the fact that you have to check for availability multiple times per day?

Me too! That's why I've created this repository: It allows you to automate your search for the current availability of sites at the Upper Pines campground.

How does it work? I'm glad you asked. It scrapes the recreation.gov website, and if a campsite is found on a certain number of consecutive days, it sends you an email with the dates available and a link to reserve your sites.

# How Do I Use It?

This tool is still under development, but it's intended use is to be run on a server like a Raspberry Pi. At the moment it uses selenium with a Firefox webdriver, so it is only compatible with that browser.

To use this tool, first download the code in the repo, then set your desired number of consecutive days in scraper.py on line 20 under "desired_conescutive_days". The default number of days is 3.

Then, fill in your email username, password, and your target email in the email_sender.py script located in the lib folder. For security reasons, I have not added these credentials to the repo by default.

Once you're all set up, just run the scraper.py script, and watch it find your campsite availability automatically! If desired, this code could be run as a cron job on a server to search multiple times per day.

# What's Next?

The roadmap for this tool includes a web UI to select desired campgrounds, dates, and consecutive number of days. Support for chromium based browsers is another option that would help more users to search for campsites.
