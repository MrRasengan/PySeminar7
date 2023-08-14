# def create_phrase(func, world):
#     print(func(world))

# def hello(s):
#     return f"Hello {s}"

# def bye(s):
#     return f"{s} bye-bye"

# create_phrase(hello, " World")
# create_phrase(hello, " Kostyan")
# create_phrase(bye, " World")
# create_phrase(bye, " Kostyan")


def calc_power(degree):
    def power(number):
        return number ** degree
    return power 

# print(calc_power(2)(3))
square = calc_power(2)
cube = calc_power(3)
print(square(8))
print(cube(3))
    