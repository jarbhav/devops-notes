import time
from functools import partial
import heavy_function
import concurrent.futures

the_sum = 0

start_time = time.time()

partial_function = partial(heavy_function.cpu_heavy.cpu_heavy_task, printout=False)
with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
  results = executor.map(partial_function, range(10))
  for i in results:
    the_sum += i

print("--- %s seconds ---" % (time.time() - start_time))

print(the_sum)