import math

print(int(20 * ((2 * (6 * 10)) + (2 * (8 * 10)))))
print(float((20 * ((2 * (6 * 10))+(2 * (8 * 10))))/(350 * 5)))


# paint problem with creating functions

HEIGHT = 10
LENGTH = 8
WIDTH = 6

big_wall = LENGTH * HEIGHT
small_wall = WIDTH * HEIGHT
room = 2 * ( big_wall + small_wall)

def total( x ,  total_number):
    return x * total_number


print(total(room, 20))