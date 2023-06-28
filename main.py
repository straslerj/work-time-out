import sys
import time

from plyer import notification


START_TIME = time.time()
NOTIFICATION_TIMEOUT = (
    30  # Duration in seconds for which the notification should be displayed
)
ONE_MINUTE_SECONDS = 60
SEVENTEEN_MINUTES_SECONDS = 17 * 60


# Screen time messages
screen_time_title = "Screen Time Alert"
screen_time_message = "You have been looking at your screen for 20 minutes. Consider looking at something 20 feet away for 20 minutes."
screen_time_icon = "resources/screen_time.ico"
screen_time_breaks = 0

# Mental break messages
mental_break_title = "Mental Break Alert"
mental_break_message = "You have been working for 52 minutes. Research shows you should take a 17 minute break to combat fatigue."
mental_break_icon = "resources/mental_break.ico"
mental_break_breaks = 0

try:
    while True:
        elapsed_minutes = int((time.time() - START_TIME) / 60)
        print(
            f"{time.strftime('[%H:%M:%S]', time.localtime())} Elapsed time: {elapsed_minutes} minutes."
        )

        if elapsed_minutes != 0 and elapsed_minutes % 1 == 0:
            print(
                f"{time.strftime('[%H:%M:%S]', time.localtime())} Screen time alert issued."
            )
            notification.notify(
                title=screen_time_title,
                message=screen_time_message,
                timeout=NOTIFICATION_TIMEOUT,
                app_icon=screen_time_icon,
            )
            screen_time_breaks += 1

        if elapsed_minutes != 0 and elapsed_minutes % 52 == 0:
            print(
                f"{time.strftime('[%H:%M:%S]', time.localtime())} Mental break alert issued."
            )
            notification.notify(
                title=mental_break_title,
                message=mental_break_message,
                timeout=NOTIFICATION_TIMEOUT,
                app_icon=mental_break_icon,
            )
            print(
                f"{time.strftime('[%H:%M:%S]', time.localtime())} Program will sleep for 17 minutes"
            )
            time.sleep(SEVENTEEN_MINUTES_SECONDS)
            mental_break_breaks += 1

        time.sleep(ONE_MINUTE_SECONDS)

except KeyboardInterrupt:
    print(
        f"\n{time.strftime('[%H:%M:%S]', time.localtime())} Program terminated.\n\t Screen time breaks taken: {screen_time_breaks}\n\tMental break breaks taken: {mental_break_breaks}"
    )
    sys.exit(0)
