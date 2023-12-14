from lib import email_sender
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
    desired_consecutive_days = 3

    sort_by_site = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "camp-sortable-column-header")))
    sort_by_site.click()     # sorts by site in ascending order to make data organization easier
    campsite_table = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "tbody")))
    
    raw_data = []

    dates = []
    for th in campsite_table.find_elements(By.XPATH, "//th"):
        for contents in th.find_elements(By.CLASS_NAME, "camp-sortable-contents"):
            for cell in contents.find_elements(By.CLASS_NAME, "date"):
                dates.append(cell.text)

    start_day = int(min(dates))
    end_day = int(max(dates)) + 1

    for tr in campsite_table.find_elements(By.XPATH, "//tr"):
        row = [cell.text for cell in tr.find_elements(By.CLASS_NAME, "rec-availability-date")]
        raw_data.append(row)
    raw_data = raw_data[2:] # removes 2 empty arrays at beginning of data

    data_table = {}

    # arrange raw data by date
    for i in range (start_day, end_day):
        data_table['Dec '+str(i)] = []
        for index,site in enumerate(raw_data): 
            data_table['Dec '+str(i)].append(site[i-start_day])
    
    # find days with availability
    available_days = 0
    days_list = []
    for item in data_table:
        if 'A' in data_table[item]:
            days_list.append(item)
            available_days += 1

    # adding "and" to the end of days_list string
    if len(days_list)>2:
        days_list = ', '.join(days_list[:-1]) + ", and " + str(days_list[-1])
    elif len(days_list)==2:
        days_list = ' and '.join(days_list)
    elif len(days_list)==1:
        days_list = days_list[0]

    if available_days >= desired_consecutive_days:
        email_sender.send_email(days_list)

finally:
    driver.quit()