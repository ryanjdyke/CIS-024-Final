import yagmail
def send_email(availability_dates):
    yag = yagmail.SMTP('SENDER'S GMAIL ADDRESS', 'PASSWORD')
    to = 'TARGET EMAIL'
    contents = [
        f"<p>Availability for {availability_dates}. Click <a href='https://www.recreation.gov/camping/campgrounds/232447'>here</a> to reserve</p>"
        ]
    yag.send('ryanjdyke@gmail.com', 'Yosemite Availability', contents)