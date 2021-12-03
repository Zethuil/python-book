# the following code returns an iterable object
# range() does not create list but generates the individual values on-demand
for i in range(3):
    print(i)


# you often need to generate a list of values without
# the need to store the actual list in memory
# the main need is to have the needed values one-by-one
# generators create iterable objects that return values in a virtual sequence
def square_generator(n):
    i = 1
    while i <= n:
        yield i * i
        i += 1


for i in square_generator(10):
    print(i, end=" ")
print()

# the function call returns an iterable object through
# which we can iterate in a for-loop
print(square_generator(10))

# main difference between return and yield
# return: go back to caller and stop function processing
# yield: store local variables and current position inside iterator
# go back to caller and re-enter the function to procees with the next step


# generators can have multiple yields
def multi_yield_generator():
    a = 10
    yield a
    yield a * 2
    b = 5
    yield a + b


for i in multi_yield_generator():
    print(i, end=" ")
print()


# we can prematurely exit a generator function by using return
def generate_names(boys=True):
    yield "Sophie"
    yield "Deirdre"
    if not boys:
        return
    yield "Barnaby"
    yield "Theodore"


print(list(generate_names()))
print(list(generate_names(False)))


# we can also call generators from within other generators
# the nested one is a sub-generator
def lads():
    yield "Barnaby"
    yield "Theodore"


def girls():
    yield "Sophie"
    yield "Deirdre"


def list_names(boys=True):
    yield from girls()
    if boys:
        yield from lads()


print(list(list_names()))
print(list(list_names(False)))
