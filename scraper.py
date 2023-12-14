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

try:
    campsite_table = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "tbody")))
    
    data = {}

    for tr in campsite_table.find_elements(By.XPATH, "//tr"):
        row = [cell.text for cell in tr.find_elements(By.CLASS_NAME, "rec-availability-date")]
        data.append(row)
    
    print(data)

finally:
    driver.quit()