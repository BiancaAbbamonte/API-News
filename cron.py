import time
import schedule
from send_email import send_email

def job():
    print("Job is running...")
    send_email()
    print("Email sent successfully!")

schedule.every().day.at("06:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
