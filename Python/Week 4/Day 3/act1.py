import timeit

print(timeit.timeit('"_".join(str(n) for n in range(100))', number=100000))
