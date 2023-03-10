def cpu_heavy_task(limit:int, printout:bool=False) -> int:
    """ a function that simulates a CPU-heavy task """

    res = 0
    for i in range(limit):
        i += 1
        res += i

    if (printout):
        print("done")

    return res