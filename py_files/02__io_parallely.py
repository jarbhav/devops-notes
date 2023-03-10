from functools import partial
import concurrent.futures

import time
import heavy_function

start_time = time.time()
the_sum = 0
partial_function = partial(heavy_function.io_heavy.io_heavy_task, printout=False)
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
  results = executor.map(partial_function, range(10))
  for i in results:
    the_sum += i
print("--- %s seconds ---" % (time.time() - start_time))

print(the_sum)
    