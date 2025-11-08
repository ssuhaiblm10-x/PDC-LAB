
import math
import time
import multiprocessing
import threading

 Function: Mensuration Calculations

def do_something(count, out_list):
    for _ in range(count):
        # Mensuration-like heavy computations
        r = 7.5
        l, b, h = 12, 8, 5
        a = 6

        # Perform multiple shape calculations
        area_circle = math.pi * r ** 2
        peri_circle = 2 * math.pi * r
        area_rect = l * b
        peri_rect = 2 * (l + b)
        area_square = a ** 2
        peri_square = 4 * a
        area_triangle = 0.5 * b * h

        # 3D calculations
        sa_cube = 6 * a ** 2
        vol_cube = a ** 3
        sa_cuboid = 2 * (l*b + b*h + h*l)
        vol_cuboid = l * b * h
        sa_cylinder = 2 * math.pi * r * (r + h)
        vol_cylinder = math.pi * r ** 2 * h

        # Artificial computation to vary timing
        total = (
            area_circle + peri_circle + area_rect + peri_rect +
            area_square + peri_square + area_triangle +
            sa_cube + vol_cube + sa_cuboid + vol_cuboid +
            sa_cylinder + vol_cylinder
        )

        # Some math work to increase CPU time
        for i in range(100):
            total += math.sqrt(total * i + 1)

        out_list.append(total)


# =====================================
# Main Program
# =====================================
if __name__ == "__main__":
    size = 50000  # smaller number to keep runtime reasonable

    print("===== MENSURATION PERFORMANCE TEST =====")
    procs = int(input("Enter number of processes: "))
    threads = int(input("Enter number of threads: "))

    # ---------- MULTIPROCESSING ----------
    jobs = []
    start_time = time.time()

    for _ in range(procs):
        out_list = []
        process = multiprocessing.Process(target=do_something, args=(size, out_list))
        jobs.append(process)

    for j in jobs:
        j.start()
    for j in jobs:
        j.join()

    end_time = time.time()
    print("\nList processing complete.")
    print("Multiprocessing time =", end_time - start_time)

    # ---------- MULTITHREADING ----------
    jobs = []
    start_time = time.time()

    for _ in range(threads):
        out_list = []
        thread = threading.Thread(target=do_something, args=(size, out_list))
        jobs.append(thread)

    for j in jobs:
        j.start()
    for j in jobs:
        j.join()

    end_time = time.time()
    print("\nList processing complete.")
    print("Multithreading time =", end_time - start_time)

