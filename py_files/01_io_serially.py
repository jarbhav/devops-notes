import time
import heavy_function
# serially


the_sum = 0

start_time = time.time()
for a_number in range(100):
    a_result = heavy_function.io_heavy.io_heavy_task(some_value=a_number, printout=False)
    the_sum += a_result

print("--- %s seconds ---" % (time.time() - start_time))

print(the_sum)
