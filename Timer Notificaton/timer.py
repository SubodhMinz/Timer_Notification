import time
from plyer import notification


while True:
    notification.notify(
        title = "Work",
        message = "This is your working time for 50 Minuts",
        timeout = 5
    )
    time.sleep(60*50)
    notification.notify(
        title = "Break",
        message = "Break for 10 Minuts",
        timeout = 5
    )
    time.sleep(60*10)
