import timeit

def disasterCode():

    prime_numbers = [2]

    for i in range (2,2500):
        uniquePrimes = []
        for n in prime_numbers:
            if i%n == 0:
                uniquePrimes.append(n)

        if not uniquePrimes:
            prime_numbers.append(i)

# Benchmark the code
if __name__ == "__main__":
    benchmark_code = "disasterCode()"
    setup_code = "from __main__ import disasterCode"

    # Measure the execution time of disasterCode function
    times = []
    for i in range(0,5):
        times.append(timeit.timeit(benchmark_code, setup=setup_code, number=1))

    res = sum(times)/5

    print(f"Average execution time after 5 runs: {res:.6f} seconds")
