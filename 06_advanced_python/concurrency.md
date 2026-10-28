# Phase 13: Multithreading & Multiprocessing — Notes

### Beginner Introduction
**The problem** — by default, Python does one thing at a time, in order. If a task has to wait (downloading a file, reading from disk, calling an API), the whole program sits idle. Concurrency lets a program make progress on other tasks instead of waiting.

**Kitchen analogy**
- **`threading`** — several cooks share one kitchen and the same ingredients. They help each other most when they are mostly *waiting* (water boiling, oven heating).
- **`multiprocessing`** — several separate kitchens, each with its own cook and ingredients. Truly simultaneous work, but more setup and no shared ingredients.
- **`asyncio`** — one very organized cook who never stands idle: starts the water, chops vegetables while it boils, and switches tasks whenever something needs waiting.
- **`concurrent.futures`** — a simpler, unified way to hire cooks (threads or processes) and collect their finished dishes.

**Key terms**
- **Process** — a running program with its own memory.
- **Thread** — a lightweight worker inside a process; threads share the process's memory.
- **I/O-bound task** — spends most time waiting (network, files, databases) → use threads or `asyncio`.
- **CPU-bound task** — spends most time computing (maths, image processing, large loops) → use processes.
- **Concurrency vs Parallelism** — concurrency is *managing* many tasks in overlapping time (may be one at a time, switching quickly); parallelism is *actually running* them at the same instant on multiple CPU cores.

### Concurrency Overview
Ways to run multiple tasks in overlapping time periods. Choose based on the workload type.
```python
threading            # I/O-bound tasks (network, files); threads share memory, limited by the GIL
multiprocessing      # CPU-bound tasks; separate processes, each with its own interpreter and memory
asyncio              # I/O-bound tasks with many connections; single thread, cooperative multitasking
concurrent.futures   # high-level interface over threads/processes
```
### Why the GIL Exists
**GIL (Global Interpreter Lock)** — a lock in CPython (the standard Python implementation) that lets only one thread execute Python bytecode at a time.

**Reference counting** — CPython tracks memory by giving every object a counter of how many references point to it. When the counter reaches 0, the object is freed immediately.
```python
import sys
sys.getrefcount(obj)     # current reference count (always +1 for the call itself)
```

**The problem** — if two threads change the same counter at the same moment (a *race condition*), the count can end up wrong:
- Count too high → memory is never freed (memory leak).
- Count too low → memory is freed while still in use (crash or corrupted data).

**The solution** — instead of locking every single object (slow, and prone to deadlocks), CPython uses *one* global lock. This keeps memory management safe, keeps single-threaded programs fast, and makes it easy to integrate C extension libraries.

**Cyclic garbage collector** — reference counting can't free objects that reference each other in a loop, so Python also runs a garbage collector to clean up these cycles.
```python
import gc
gc.collect()             # manually trigger garbage collection
```

**What this means in practice**
- Threads don't speed up CPU-bound code, because only one runs Python code at a time.
- Threads still help with I/O-bound code, because the GIL is released while waiting on network/disk.
- `multiprocessing` bypasses the GIL, because each process has its own interpreter and its own GIL.
- Libraries like NumPy release the GIL during heavy C-level computation.
- Recent Python versions (3.13+) offer an optional *free-threaded* build that removes the GIL.

### `threading`
Runs multiple threads within the same process, sharing the same memory space. Best suited for I/O-bound tasks where threads spend time waiting.
```python
import threading

t = threading.Thread(target=function_name, args=(arg1, arg2))
t.start()                        # start the thread
t.join()                         # wait for the thread to finish
t.daemon = True                  # daemon thread exits with the main program
threading.current_thread()
```
**Synchronization tools** — prevent race conditions when threads share data.
```python
lock = threading.Lock()
with lock:
    ...                          # critical section

threading.RLock()                # re-entrant lock
threading.Semaphore(n)           # limit concurrent access to n threads
threading.Event()                # signal between threads (.set(), .wait(), .clear())
```

### `multiprocessing`
Runs tasks in separate processes, each with its own memory and Python interpreter, bypassing the GIL. Best suited for CPU-bound tasks.
```python
import multiprocessing

if __name__ == "__main__":           # required on Windows/macOS
    p = multiprocessing.Process(target=function_name, args=(arg1,))
    p.start()
    p.join()
```
**Process pool** — manages a pool of worker processes.
```python
from multiprocessing import Pool

with Pool(processes=n) as pool:
    results = pool.map(function, iterable)
    result = pool.apply(function, args)
    pool.apply_async(function, args)
```
**Sharing data between processes** — memory isn't shared by default.
```python
multiprocessing.Queue()              # message passing
multiprocessing.Pipe()               # two-way connection
multiprocessing.Value(type, value)   # shared single value
multiprocessing.Array(type, values)  # shared array
multiprocessing.Lock()
```

### `concurrent.futures`
A high-level interface for running tasks asynchronously using thread or process pools, returning `Future` objects that represent pending results.
```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=n) as executor:
    future = executor.submit(function, arg1, arg2)
    result = future.result()                       # blocks until done
    results = executor.map(function, iterable)     # results in input order

# handle results as they finish
futures = [executor.submit(function, x) for x in items]
for future in as_completed(futures):
    result = future.result()

# same API for CPU-bound tasks
with ProcessPoolExecutor(max_workers=n) as executor:
    ...
```

### Async Programming (`asyncio`)
Runs many tasks concurrently in a single thread using an event loop. Tasks voluntarily pause at `await` points so other tasks can run. Best for high-volume I/O-bound work such as network requests.
- **`async def`** — defines a coroutine function.
- **`await`** — pauses the coroutine until the awaited operation completes.
- **Event loop** — schedules and runs coroutines.
```python
import asyncio

async def coroutine_name():
    await asyncio.sleep(seconds)
    return value

asyncio.run(coroutine_name())                    # entry point
```
**Running multiple coroutines concurrently**
```python
results = await asyncio.gather(coro1(), coro2(), coro3())

task = asyncio.create_task(coroutine_name())     # schedule a coroutine
await task

await asyncio.wait_for(coro(), timeout=seconds)  # timeout handling
```
**Async iteration and context managers**
```python
async with resource as r:
    ...

async for item in async_iterable:
    ...
```
**Synchronization**
```python
asyncio.Lock()
asyncio.Semaphore(n)
asyncio.Queue()
```