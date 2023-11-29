import time
import threading

class Clock:
    def __init__(self):
        self._stop_event = threading.Event()
        self._clock_thread = threading.Thread(target=self._run)

    def start(self):
        self._stop_event.clear()
        self._clock_thread.start()

    def stop(self):
        self._stop_event.set()

    def _run(self):
        h, m, s = 0, 0, 0
        while not self._stop_event.is_set():
            print("\r{:02d}:{:02d}:{:02d}".format(h, m, s), end="")
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

clock = Clock()
clock.start()  # Start the clock
time.sleep(5)  # Let the clock run for 5 seconds
clock.stop()  # Stop the clock
