'''
Reverse a stack of integers using recursion, where the last element is the TOP most element of the stack
Output format: first integer i.e. index = 0 denotes the TOP element of the reversed stack
Qn link: https://www.ambitionbox.com/interviews/amdocs-question/reverse-stack-using-recursion-reverse-a-given-stack-of-integers-using-recursion-note-you-are-not-allowed-to-use-any-extra-space-other-than-the-internal-stack-space-used-due-jvg48wyX?campaign=company_interview_page_view_answer
'''
def reverse_stack(stack):
    if len(stack) == 0:
        return []
    else:
        top_element = stack.pop(0) # start removing elements from index 0 so that whenever the function returns the recursive call it will start from the last element of the stack passed in which is the TOP
        reverse_stack(stack)
        insert_at_bottom(stack, top_element)
        return stack

def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
    else:
        top_element = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(top_element)


print(reverse_stack([2, 1, 3]))