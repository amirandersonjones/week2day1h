#Find Even numbers
#Create a function that, given a list as a parameter, finds the even numbers inside the list. The function should then return a list.
#Example:
#Input: [2, 7, 10, 11, 12]
#Output: [2, 10, 12]

def my_func(evennumbers):
    numbers= []
    for number in evennumbers:
        if number % 2 == 0:
            numbers.append(number)
    print(numbers)
my_func([2, 7, 10, 11, 12, 5, 8])