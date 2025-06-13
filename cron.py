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
    
#
# Make sure to run this script in an environment where it can run indefinitely,
# such as a terminal or a background process.
# If you want to run this script as a cron job, you can create a cron entry
# that executes this script at the desired interval.
# For example, to run this script every minute, you can add the following line
# to your crontab:
# * * * * * /usr/bin/python3 /path/to/your/script.py
# Make sure to replace `/usr/bin/python3` with the path to your Python interpreter
# and `/path/to/your/script.py` with the path to this script.
# Note: The above cron entry will run the script every minute, not every 10 seconds.
# If you want to run it every 10 seconds, you would need to use a different approach,
# such as using a while loop with a sleep interval, as shown in the code above.
# Alternatively, you can use a task scheduler like Celery or APScheduler for more complex scheduling needs.
# This code sets up a simple job scheduler that runs a job every 10 seconds.
