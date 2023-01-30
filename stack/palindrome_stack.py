'''
O(n) complexity

'''

import stack

s = stack.Stack()

text = input("Please input a palindrome: ")
# convert to lowercase
text = text.lower()

# push each char into stack
for each_char in text:
    s.push(each_char)

# reverse each_char in the stack
reverse_str = ""

while not s.is_empty():
    reverse_str = reverse_str + s.pop()

if text == reverse_str:
    print("Palindrome found!")
else:
    print("Sorry, this word is not a palindrome :(")