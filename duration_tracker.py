from time import sleep
import random
from datetime import datetime
import itertools as it

def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0,0.2))
        yield datetime.now()-starttime

def tracker(prod, limit=1):
    """Track how many times producer yields an odd-number of seconds.
    """
    count = 0
    while count < limit:
        # Get next timedelta from the producer
        dt = next(prod)

        # If seconds is odd, increment the count
        if dt.seconds % 2 == 1:
            count += 1

        # Yield current count and optionally receive a new limit
        new_limit = (yield count)
        if new_limit is not None:
            limit = new_limit
