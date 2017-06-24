from datetime import datetime
from datetime import timedelta
import time
import alert_functions

while True:

    alert_functions.send_alert_message()

    dt = datetime.now() + timedelta(hours=3)

    while datetime.now() < dt:
        time.sleep(1)

