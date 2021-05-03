# created/revised by <Osmig Torres> on <5/2/2021>

###################
#    FizzBuzz!    #
###################

# display Fizz alongside numbers divisible by 3, and buzz when divisible by 5
# at the end it displays the amount of fizz, buzz, and fizzbuzz.

num = 1
fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

while num <= 100:
    if (num % 3 == 0) and (num % 5 == 0):
        print(str(num) + ". Fizzbuzz!")
        fizzbuzz_count += 1

    elif num % 3 == 0:
        print(str(num) + ". Fizz!")
        fizz_count += 1

    elif num % 5 == 0:
        print(str(num) + ". Buzz!")
        buzz_count += 1

    else:
        print(str(num) + ".")

    num += 1

print("____________________________")
print("Fizz\t\tBuzz\t\tFizzbuzz")
print(str("({:,})".format(fizz_count)) + "\t\t" + str("({:,})".format(buzz_count)) + "\t\t" + str("({:,})".format(fizzbuzz_count)))

