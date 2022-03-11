"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

"""


def isValid(s):

    stack = []

    if len(s) == 0:
        return False
    lefts = ['(', '{', '[']
    rights = [')', '}', ']']

    for i in range(len(s)):
        if len(stack) == 0 and s[i] in lefts:
            stack.append(s[i])
        elif len(stack) == 0 and s[i] in rights and s[i] not in lefts:
            return False
        elif len(stack) >= 1 and stack[-1] in lefts and s[i] in rights:
            if s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[i] == '}' and stack[-1] == '{':
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
        else:
            stack.append(s[i])
    if len(stack) == 0:
        return True
    else:
        return False