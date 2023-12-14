from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
options = Options()
options.set_preference('profile', '/Users/ryanjdyke/Library/Application Support/Firefox/Profiles/gqpn7hxe.default-release')
service = Service('/usr/local/bin/geckodriver')
driver = Firefox(service=service, options=options)
driver.set_window_size(1920, 1080)
driver.get("https://www.recreation.gov/camping/campgrounds/232447")