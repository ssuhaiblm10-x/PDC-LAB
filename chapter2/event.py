
import math
import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
event = threading.Event()

# ========================
# Mensuration Calculations
# ========================
def mensuration_calculations():
    r = 7.5
    l, b, h = 12, 8, 5
    a = 6

    area_circle = math.pi * r ** 2
    peri_circle = 2 * math.pi * r
    area_rect = l * b
    peri_rect = 2 * (l + b)
    area_square = a ** 2
    peri_square = 4 * a
    area_triangle = 0.5 * b * h

    sa_cube = 6 * a ** 2
    vol_cube = a ** 3
    sa_cuboid = 2 * (l*b + b*h + h*l)
    vol_cuboid = l * b * h
    sa_cylinder = 2 * math.pi * r * (r + h)
    vol_cylinder = math.pi * r ** 2 * h

    total = (
        area_circle + peri_circle + area_rect + peri_rect +
        area_square + peri_square + area_triangle +
        sa_cube + vol_cube + sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )

    return total


# ========================
# Multithreading Classes
# ========================
class Consumer(threading.Thread):
    def run(self):
        while True:
            time.sleep(2)
            event.wait()
            if items:
                item = items.pop()
                logging.info(f'Consumer notify: {item} popped by {self.name}')


class Producer(threading.Thread):
    def run(self):
        for i in range(5):   # Producing item 5 times
            time.sleep(2)
            result = mensuration_calculations()   # Use the mensuration total
            items.append(result)
            logging.info(f'Producer notify: Calculated total {result:.2f} appended by {self.name}')
            event.set()
            event.clear()


# ========================
# Main Execution
# ========================
if __name__ == "__main__":
    t1 = Producer()
    t2 = Consumer()

    t1.start()
    t2.start()

    t1.join()
    t2.join()
