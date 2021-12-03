# an iterator is an abstraction for enumerating elements of
# a container (object instance) via a standardised interface
# every iterable instance must implement __iter__(self)
# a __next__(self) must be implemented
# on reaching the end, __next__ must throw a StopIteration exception
class Fibonacci:
    def __init__(self, max_n):
        self.MaxN = max_n
        self.N = 0
        self.A = 0
        self.B = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.N < self.MaxN:
            self.N += 1
            self.A, self.B = self.B, self.A + self.B
            return self.A
        else:
            raise StopIteration


# simple application as with generators (every generator IS an iterator)
print(list(Fibonacci(4)))

my_instance = Fibonacci(5)
iterator1 = iter(my_instance)
print(next(iterator1))

iterator2 = iter(my_instance)
print(next(iterator1), next(iterator1))
print(next(iterator2), next(iterator2))
