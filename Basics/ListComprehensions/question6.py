# Write a comprehension that goes through numbers 1–20 and replaces
# multiples of 3 with 'Fizz', multiples of 5 with 'Buzz', multiples of both
# with 'FizzBuzz', and keeps the number otherwise.

numbers = [ 
    "FizzBuzz" if i % 15 == 0 else
    "Fizz" if i % 3 == 0 else
    "Buzz" if i % 5 == 0 else
    i
    for i in range(1, 21)
]

print(numbers)