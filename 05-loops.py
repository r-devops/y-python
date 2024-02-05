# Two Loops
#   1. For Loop
#   2. While Loop

# Syntax - for loop
# for var in values:
#   statements

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print("Fruit Name -", fruit)

# Syntax - While Loop
# while (expression):
#   statements

count = 10
while(count > 0):
    count = count -1
    print("Count - ", count)

# while supports else as well

count = 10
while(count > 0):
    count = count -1
    print("Count - ", count)
else:
    print("End of Loop")
