# Python program
#that will output all even numbers
# between 1 and 50

# Determine the range
start = 1
end = 50

# Using a for loop to print the even numbers
for i in range(start+1, end+1, 2):
    print(i)

# Using list comprehension to find the event numbers
res = [i for i in range(start, end+1) if i % 2 == 0]
 
#Print the list of even numbers
print(res)


        
# Using a for loop to print the even numbers
for i in range(start, end+1):
    if i % 2 == 0:
        print(i)
 



