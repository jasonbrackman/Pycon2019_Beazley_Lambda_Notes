import time
import cProfile


def expensive_op():
    for _ in range(100):
        time.sleep(0.01)


if __name__ == "__main__":
    profile = cProfile.Profile()
    profile.runcall(expensive_op)
    profile.print_stats()

    cProfile.run('expensive_op()', '.')
