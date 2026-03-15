# Write a function fizzbuzz(n) that prints numbers 1 to n, but replaces multiples of 3 with 'Fizz',
# multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'. Then generalise it:
# fizzbuzz_custom(n, rules) where rules is a list of (divisor, word) pairs, so you can add your own
# rules.

#checking the multiplication
# def mul(n):
#     for i in range(1, 11):
#         print(f"{n} * {i} = {n*i}")

# mul(3)


# def fizzbuzz(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# fizzbuzz(15)


# Custom Version (Generalised)
def fizzbuzz_custom(n, rules):
    for i in range(1, n+1):
        output = ""

        for divisor, word in rules:
            if i % divisor == 0:
                output += word

        if output == "":
            print(i)
        else:
            print(output)

rules = [(3,"Fizz"), (5,"Buzz")]

fizzbuzz_custom(15, rules)

# Why this version is powerful
# You can add any rule.
rules = [(3,"Fizz"), (5,"Buzz"), (7,"Pop")]
fizzbuzz_custom(21, rules)