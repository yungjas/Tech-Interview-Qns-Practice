'''
O(1) complexity

Comparsion. For instance, we have two variables a and b. And when we doing this a==b we just take a and b from the memory and compare them. 

Let's define "c" as cost of memory, and "t" as cost of time. 

In this case we're using 2c (because we're using two cells of the memory) and 1t (because there is only one operation with the constant cost), 
therefore the 1t - is the constant. 

Thus the time complexity is constant

https://stackoverflow.com/questions/59394539/what-is-the-time-complexity-of-a-comparison-or-substitution-operation

'''

str1 = "dAd"
# convert to lowecase, lower method returns a string that consits of all lowecase letters
str1 = str1.lower()

str2 = str1[::-1]

if str1 == str2:
    print("Palindrome found!")
else:
    print("Sorry, this word is not a palindrome :(")