from time import time
from functools import wraps
from random import randint

class Chrono():
    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return decorated
    def __enter__(self):
        self.time = time()      
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.time = time() - self.time
        print("temps d'exécution: " + str(self.time))

@Chrono()
def tri(lst):
    for a in range(len(lst)):
        nb = lst[a]
        ind = a
        for b in range(a, len(lst)):
            if nb > lst[b]:
               nb = lst[b]
               ind = b
        lst[ind] = lst[a]
        lst[a] = nb
    return lst


print(tri([randint(0, 1000000000) for a in range(1000)]))
print(tri([randint(0, 1000000000) for a in range(1000)]))
print(tri([randint(0, 1000000000) for a in range(1000)]))
