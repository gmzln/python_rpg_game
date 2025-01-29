import threading

def start_timer(duration):
    event = threading.Event()
    def time_out():
        event.set()
    timer = threading.Timer(duration, time_out)
    timer.start()
    return timer, event