import yagmail

sender_address = "INSERT YOUR SENDER GMAIL HERE" # Must be a gmail account
password = "INSERT PASSWORD HERE" # Password for sender gmail account
receiver_address = "INSERT RECEIVER EMAIL HERE" # Can be any email

def send_email(availability_dates):
    yag = yagmail.SMTP(sender_address, password)
    to = receiver_address
    contents = [
        f"<p>Availability for {availability_dates}. Click <a href='https://www.recreation.gov/camping/campgrounds/232447'>here</a> to reserve</p>"
        ]
    yag.send(to, 'Yosemite Availability', contents)