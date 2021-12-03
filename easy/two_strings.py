'''
Given two strings, determine if they share a common substring. A substring may be as small as one character.

Example:
s1 = "and"
s2 = "art"
These share the common substring a

s1 = "be"
s2 = "cat"
These do not share a substring.

Function Description
twoStrings has the following parameter(s):
    string s1: a string
    string s2: another string

Returns:
    string: either YES or NO

'''
# Help from: https://stackoverflow.com/questions/48611525/find-common-characters-between-two-strings

def twoStrings(s1, s2):
    result = "".join(set(s1).intersection(s2))
    if len(result) > 0:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
	print(twoStrings("hi", "world"))