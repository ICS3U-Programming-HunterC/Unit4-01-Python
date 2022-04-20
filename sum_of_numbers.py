#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: April 19, 2022
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum 
# of all numbers from 0 until that number.


import random
import math


def main():
    # declare varibles
    loop_num = 0
    sum = 0

    # Get the user input as a string
    user_input_string = input("Enter a positive number: ")
    print("")

    # calculate the sum of the numbers from 0 to the user input
    try:
        user_input = int(user_input_string)

        if user_input < 0:
            print("That is a negative number")

        while loop_num < user_input:
            loop_num = loop_num + 1
            print("{0} times through loop".format(loop_num))
            sum = sum + loop_num
        print("")
        print(
            "The total sum of the numbers from 0 to {} is: {}".format(user_input, sum)
        )

    except Exception:
        print("That is not a number!!")


if __name__ == "__main__":
    main()
