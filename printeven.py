#Write a python program to print even numbers in a list.


list1 = [11, 23, 45, 23, 64, 22, 11, 24]

# iteration
for num in list1:
    # check
    if num % 2 == 0:
        print(num, end=" ")