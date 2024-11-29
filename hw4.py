#Task 1
import random

number = random.randint(1,10)
user_number = int(input("Let's try to guess a number: "))
print(number)
if user_number==number:
    print("You're lucky!")
else:
    print("Let's try again!")

#Task 2

name = input("Write your name here: ")
age = int(input("Write your age here, please: "))

print("Hello {}, on your next birthday you'll be {}".format(name, age+1))

#Task 3

input_string = input("Enter a string: ")

length_of_input = len(input_string)

random_strings = []

for i in range(5):
    
    random_string = ''.join(random.sample(input_string, length_of_input))
    random_strings.append(random_string)


for idx, random_string in enumerate(random_strings, start=1):
    print(f"Random string {idx}: {random_string}")

