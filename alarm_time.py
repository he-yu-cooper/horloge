import time

def display_time(h, m, s):
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)

def set_alarm(h, m, s):
    alarm_time = (h, m, s)
    return alarm_time

def main():
    h, m, s = map(int, input("Enter the time (format: hours minutes seconds): ").split())
    alarm_h, alarm_m, alarm_s = map(int, input("Enter the alarm time (format: hours minutes seconds): ").split())
    alarm_time = set_alarm(alarm_h, alarm_m, alarm_s)
    while True:
        print("\r" + display_time(h, m, s), end="")
        time.sleep(1)
        s += 1
        if s == 60:
            s = 0
            m += 1
        if m == 60:
            m = 0
            h += 1
        if h == 24:
            h = 0
        if (h, m, s) == alarm_time:
            print("\nAlarm time!")
            break

if __name__ == "__main__":
    main()