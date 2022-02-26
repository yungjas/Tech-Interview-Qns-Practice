str1 = "dAd"
# convert to lowecase, lower method returns a string that consits of all lowecase letters
str1 = str1.lower()

str2 = str1[::-1]

if str1 == str2:
    print("Palindrome found!")
else:
    print("Sorry, this word is not a palindrome :(")