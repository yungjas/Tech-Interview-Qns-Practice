def isBalanced(s):
    # Write your code here
    stack = []
    
    for each_bracket in s:
        if each_bracket != "}" and each_bracket != ")" and each_bracket != "]":
            stack.append(each_bracket)
        elif each_bracket == "}" and stack.pop() != "{":
            return "NO"
        elif each_bracket == ")" and stack.pop() != "(":
            return "NO"
        elif each_bracket == "]" and stack.pop() != "[":
            return "NO"
    
    return "YES"

print(isBalanced("{[(])}"))