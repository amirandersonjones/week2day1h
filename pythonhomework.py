#Exercise 3
#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age=int(input('Hello, please tell me your age!'))
if age <= 18:
    print('You are a kid!')
elif age <= 65:
    print('You are a good looking adult!')
else:
    print('Senior!')

#Exercise #2
#Get first prime numbers up to 100



Exercise #1
Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)


