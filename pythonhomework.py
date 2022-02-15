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
#loop through the numbers 0-100
#check if they are divisble by any preceeding numbers.

for num in range(101):
    for div in range(2, num):
        if num % div == 0: #if this is true, not a prime number.
            break

    else:
        print(num)


#Exercise #1
#Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.
#print the cubed version of 0-10 and print the cude of each

cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)


for num in range(11):
    print(num**3)