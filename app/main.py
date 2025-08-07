from typing import Callable


def cache(func: Callable) -> Callable:
    stored_cache = {}

    def validation(*args) -> Callable:
        if args in stored_cache:
            print("Getting from cache")
            return stored_cache[args]
        else:
            print("Calculating new result")
            stored_cache[args] = func(*args)
            return stored_cache[args]

    return validation
