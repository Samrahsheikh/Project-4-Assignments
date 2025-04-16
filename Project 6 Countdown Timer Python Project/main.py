import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(f"\rTime Remaining: {timer}", end="")
        time.sleep(1)
        seconds -= 1
    print("\rTime's up!")

try:
    total_time = int(input("Enter time in seconds: "))
    countdown_timer(total_time)
except ValueError:
    print("Please enter a valid number.")
