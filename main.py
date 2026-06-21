import sys
from time import time
from sorter import sort_files
from factorize import factorize_sync, factorize_parallel


def run_sorter():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до директорії!")
        return

    src = sys.argv[1]
    dist = sys.argv[2] if len(sys.argv) > 2 else "dist"

    sort_files(src, dist)


def run_factorize():
    nums = [128, 255, 99999, 10651060]

    start = time()
    sync_res = factorize_sync(*nums)
    print("Sync:", time() - start)

    start = time()
    par_res = factorize_parallel(*nums)
    print("Parallel:", time() - start)

    print(sync_res)
    print(par_res)


if __name__ == "__main__":
    choice = input(
        '1 - sorter\n'
        '2 - factorize\n'
    )

    if choice == "1":
        run_sorter()

    if choice == "2":
        run_factorize()

