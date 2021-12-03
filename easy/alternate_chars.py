'''
You are given a string containing characters A and B only. 

Your task is to change it into a string such that there are no matching adjacent characters i.e. each character in the resulting string needs to be alternating. 

To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

Example:
s = AABAAB
Remove A at positions 0 and 3 to make s = ABAB in 2 deletions

Function Description:
alternatingCharacters takes in a string s
'''

def alternatingCharacters(s):
    # Write your code here
    delete = 0
    for i in range(len(s)):
        if i != len(s) - 1:
            # if current character is the same as the next character, it means that there are adjacent characters --> DELETE
            if s[i] == s[i+1]:
                delete += 1
    return delete

if __name__ == "__main__":
	print(alternatingCharacters("AAABBB"))