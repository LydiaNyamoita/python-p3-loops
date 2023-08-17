#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
      print (i)
      i -= 1
      print("Happy New Year!")
    # code goes here!
    

def square_integers(int_list):
    new_list=[]
    for n in int_list:
        new_list.append(n * n)
    return new_list



def fizzbuzz():
    # code goes here!
    for i in range(100):
        if  i%3 == 0 and i%5 == 0:
            print ("FizzBuzz")
        elif i%5 == 0:
            print("Buzz")
        elif i%3 == 0:
            print ("Fizz")
        else:
            print(i)



print(fizzbuzz())
 
 
