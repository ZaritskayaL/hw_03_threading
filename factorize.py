from multiprocessing import Pool, cpu_count


def factorize_number(n: int) -> list[int]:
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


def factorize_sync(*numbers):
    return [factorize_number(n) for n in numbers]


def factorize_parallel(*numbers):
    with Pool(cpu_count()) as pool:
        return pool.map(factorize_number, numbers)
