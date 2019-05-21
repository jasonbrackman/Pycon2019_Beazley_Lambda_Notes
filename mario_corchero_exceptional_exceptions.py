import dis
# Anything can be marked as exception
# - This means you can have a bug where somthing will never be caught.


# This is curious
def curious_return():
    # for some reason Python doesn't return the the 1 but the 4.
    # - The talk didn't go into it -- but asks the viewers instead to use dis.dis
    #
    try:
        return 1
    except:
        return 2
    else:
        return 3
    finally:
        return 4


assert curious_return() == 4

# So what does the dis.dis show?
# - Looks like the setup_finally is actually added first, so its evaluated first and
# - never gives an opportunity to return the first return in the 'try' block.
dis.dis(curious_return)


def test_02():
    def remove_exception_history():
        try:
            1/0
        except Exception:
            # Note how the built in divide by zero info is now overwritten
            # - This is useful if you are attempting to hide or implement your own Exception
            # - interface and hiding the implementation details behind the scenes.
            raise Exception("Can divide like that.") from None

    remove_exception_history()

# -- This will create exception, but won't be clear from what thread the exception was thrown.
# import threading
# threading.Thread(target=lambda: 1/0).start()

# -- this will populate the exception from the thread to the main program.
# import concurrent.futures
# with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
#     future = executor.submit(lambda: 1/0)
#     future.result()

