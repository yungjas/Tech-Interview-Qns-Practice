import queuee

q = queuee.Queuee()

text = input("Please input a palindrome: ")
text = text.lower()

for each_char in text:
    q.enqueue(each_char)

reverse_str = ""

while not q.is_empty():
    reverse_str = reverse_str + q.dequeue()
print(reverse_str)

if reverse_str == text:
    print("Palindrome found!")
else:
    print("Sorry, this word it not a palindrome :(")