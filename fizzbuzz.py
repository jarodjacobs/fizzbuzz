""""Write a program that prints the numbers from 1 to 100.
But for multiples of three print Fizz instead of the number and for the multiples of five print Buzz.
For numbers which are multiples of both three and five print FizzBuzz."""

for num in range(1, 101):
    fizzbuzz_list = []
    if (num % 3 == 0) and (num % 5 == 0):
        fizzbuzz_list.append ("FizzBuzz")
    elif (num % 3 == 0):
        fizzbuzz_list.append ("Fizz")
    elif (num % 5 == 0):
        fizzbuzz_list.append ("Buzz")
    else:
        fizzbuzz_list.append (num)
    print(fizzbuzz_list)

       
