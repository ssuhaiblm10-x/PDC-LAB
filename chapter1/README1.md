# PDC-LAB
PDC ASSIGNMENT
CHAPTER 01:



Multiprocessing vs Multithreading

Multithreading means running multiple threads within a single process. All threads share the same memory space, which makes communication fast but can lead to data corruption if not managed properly. It’s most effective for I/O-bound tasks, such as reading files, handling web requests, or waiting for user input. However, in Python, threads are limited by the Global Interpreter Lock (GIL), so only one thread executes Python code at a time.

Multiprocessing, on the other hand, involves running multiple processes simultaneously. Each process has its own memory space and interpreter, so they can truly run in parallel on multiple CPU cores. It’s ideal for CPU-bound tasks, such as mathematical computations, data analysis, or image processing. Communication between processes is slower and more complex than between threads, but they are completely independent—if one crashes, others are unaffected.

Summary

Multithreading: Many threads share one memory; best for I/O-bound tasks.
Multiprocessing: Many processes with separate memory; best for CPU-bound tasks.
Threading saves memory but is limited by the GIL (in Python).
Processing uses more resources but achieves true parallelism.

