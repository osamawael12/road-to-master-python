# Exercise 01
age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


# Exercise 02
score = float(input("Enter score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# Exercise 03
sales = 750000
target = 800000

if sales >= target:
    print("Target Achieved")
else:
    print("Target Not Achieved")


# Exercise 04
spending = float(input("Enter spending: "))

if spending >= 10000:
    print("VIP")
elif spending >= 5000:
    print("Premium")
elif spending >= 1000:
    print("Regular")
else:
    print("Basic")


# Exercise 05
age = int(input("Enter age: "))
experience = int(input("Enter experience: "))

if age >= 21 and experience >= 2:
    print("Eligible")
else:
    print("Not Eligible")