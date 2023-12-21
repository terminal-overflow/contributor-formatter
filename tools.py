import sys
import time
from threading import Thread

class Loader():
    """ Displays loading text when called """
    def __init__(self):
        self.loading = False

    def start_loading(self):
        self.loading = True

        def load_start():
            sys.stdout.write('fetching user data')

            while self.loading:
                sys.stdout.write('.')
                sys.stdout.flush()
                time.sleep(1)

        t = Thread(target= load_start)
        t.start()

    def stop_loading(self):
        self.loading = False
        sys.stdout.write('\n')