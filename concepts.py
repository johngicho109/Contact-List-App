# import this
import random, math

def circle_circumference():
    """
    A function that calculates the circumference of circle
    """
    r = random.randint(0, 10)
    return r* math.pi * 2

def BMI(height, weight):
    """
    A function that returns a BMI value
    """
    return weight / height

def loan_calc(income, loan):
    """
    A fuction that return the time it takes to pay a loan given that he/she pays 25% of the income
    """
    amount_payable = 0.25 * income
    print(amount_payable)
    return loan / amount_payable

def birth_day():
    age = int(input("Enter your age: "))
    return 2022 - age

def years80():
    return birth_day + 80

def tip_calc():
    bill = input("Enter the bill: ")
    tip = 0.15 * bill
    total_cost = bill + tip
    return total_cost

def loop_list():
    l1 = [1,2,3,4,5]
    for i in range(len(l1),10):
        print(i)

loop_list()

def count_characters():
    input_string = "Enter a string"
    characters = {}
    for character in input_string:
        characters.setdefault(character, 0)
        characters[character] += 1

    print(characters)

def greetings():
    first_name = "Joe"
    last_name = "Tech"
    age = 26
    print(f"My name is {first_name} {last_name} and i am aged {age}")
    print(r"Relationship\"s Goals")

greetings()

count_characters()  

a = circle_circumference()
print("Circumference is: ", a)

t1 = loan_calc(15000,150000)
print(t1)

print("I am first\'s one on the list")
print(r"I am first\'s one on the list")

handle = open("text.txt","r")
data = handle.read()
print(data)
handle.close()

print("-"*20)
handle2 = open("text.txt","r")
data2 = handle2.readline()
print(data2)
handle2.close()

print("-"*20)
handle3 = open("text.txt","r")
data3 = handle3.readlines()
print(data3)
handle3.close()

print("-"*20)
handle4 = open("notes.txt","r")
data4 = handle4.read()
counter = 0
for word in data4.split():
    if word == "python":
        counter += 1
print(counter)
handle4.close()

with  open("write_text.txt","w") as handle5:
    handle5.write("Hello world")
