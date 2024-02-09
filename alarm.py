import datetime
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Alarm! Alarm! Alarm!")
            winsound.Beep(1000, 1000) 
            break
        time.sleep(1)

def main():
    print("Welcome to Alarm Clock!")
    print("Please input the time in 24-hour format (e.g., 13:30)")
    alarm_time = input("Enter the time for the alarm: ")
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M")
    except ValueError:
        print("Invalid time format! Please use HH:MM")
        return

    print(f"Alarm set for {alarm_time}")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
