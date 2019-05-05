import time
import cProfile
import pstats


def expensive_op():
    for _ in range(100):
        time.sleep(0.01)


def use_cprofile_on_function():
    """Example of how to profile and get info right away."""
    profile = cProfile.Profile()
    profile.runcall(expensive_op)
    profile.print_stats()

    cProfile.run('expensive_op()', '.')


def use_cprofile_to_store_results():
    """
    Example of profiling to storage to be reviewed later.
        In post-mortem you can review the results
        --> In some cases teams have written decorators to save out these profiles to
        --> be reviewed at a later time.
    """
    # First Option is the function name
    # Second Option is the name used to save the file out
    cProfile.run("expensive_op()", "fast.stats")


def pstats_analysing_offline_file():
    """Example of feeding a file to pstats and viewing different pieces of info."""
    stats = pstats.Stats("fast.stats")
    stats.print_stats()  # exactly what the cProfile example that prints to screen does
    stats.print_stats(3)  # print only the first three stats
    stats.print_stats("calls")  # information about the number of calls

    # Example of directional caller/callee stats.
    stats.print_callers()
    stats.print_callees("expensive_op")


def python37_timing_options():
    # Python 3.7 or later feature
    start1 = time.perf_counter()  # Wall Clock Timing (in ns)
    start2 = time.process_time()  # CPU timing
    for _ in range(1_000):
        time.sleep(0.001)
    end1 = time.perf_counter()
    end2 = time.process_time()

    print(start1 - end1)  # wall clock result
    print(start2 - end2)  # cpu time result

if __name__ == "__main__":
    pass
