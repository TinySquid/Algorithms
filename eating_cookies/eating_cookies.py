import sys


def eating_cookies(n, cache={}):
    """
    n - int - Number of cookies in the jar
    cache - list - memoization of cookie methods already calculated
    """

    count = 0

    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = (
                eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
            )
            return cache[n]
    return count


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(
            "There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
                ways=eating_cookies(num_cookies), n=num_cookies
            )
        )
    else:
        print("Usage: eating_cookies.py [num_cookies]")

