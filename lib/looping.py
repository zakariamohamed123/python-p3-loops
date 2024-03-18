#!/usr/bin/env python3


def happy_new_year():
    # code goes here!
    countdown = 10
    while countdown in range(10, 0, -1):
        print(countdown)
        countdown -= 1
    
    print("Happy New Year!")

     
    
def square_integers(int_list):
    # code goes here!
    return [i ** 2 for i in int_list]

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)