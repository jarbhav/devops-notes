import time

def io_heavy_task(some_value:int, printout:bool=False) -> int:
    """ A function that simulates an IO heavy task """

    time.sleep(2)
    if (printout):
            print('done')
    return some_value * 2