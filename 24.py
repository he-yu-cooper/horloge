import time

def display_time(h, m, s):
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)

def main():
    h, m, s = 0, 0, 0
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

if __name__ == "__main__":
    main()
