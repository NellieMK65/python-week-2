""" Control Flow - depends on boolean expressions -> expressions that evaluate to True/False
-> The order of execution
-> We are able to control the said order
"""

# Conditional statements

age = 37

if age > 18: # the if only checks for truthy
    print("You are an adult")
else:
    print("You are a kid")

# multiple conditions using ternary operator
message = "Kid" if age < 18 else \
          "Adult" if age >= 18 else \
          "Third floor" if age >= 30 and age <= 49 else \
          "Above 50"


score = 67

if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Grade D")

def grader(score):
    # this checks for falsy
    if score < 0 or score > 100:
        return "Invalid score. Has to be between 100 and 0"

    if score >= 90:
        return "Grade A"

    # this checks for truthy
    if score >= 0 and score <= 100:
        # check for grade
        if score >= 90:
            return "Grade A"
    else:
        return "Invalid score. Has to be between 100 and 0"


# Loops using for loop
colors = ['red', 'green', 'blue']

# for color in colors:
#     print(color)


# range -> in built function that generates a sequence of numbers
for i in range(len(colors)):
    print(colors[i])


count = 0

# while loops execute blocks of code repeatedly as long as the given
# condition is true
while count < 5:
    print(count)
    count += 1

print("Below the while loop")
