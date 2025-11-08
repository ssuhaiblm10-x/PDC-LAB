import math
from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

# -----------------------------------------
# Mensuration Calculations Function
# -----------------------------------------
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

# -----------------------------------------
# Thread Race Code With Mensuration Included
# -----------------------------------------
num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']

def runner(name):
    sleep(randrange(2, 5))
    print(f'{name} reached the barrier at: {ctime()}')
    
    # Call Mensuration Calculation
    result = mensuration_calculations()
    print(f'{name} calculated mensuration total = {result:.2f}\n')
    
    finish_line.wait()

def main():
    threads = []
    print('START RACE!!!!\n')
    
    for name in runners:
        t = Thread(target=runner, args=(name,))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()
    
    print('\nRace over!')

if __name__ == "__main__":
    main()
