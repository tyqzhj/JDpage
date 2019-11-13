#!/usr/bin/env python3
from stack import Stack
def balanced_parentheses(parentheses):
    stack = Stack(len(parentheses))
    for parenthesis in parentheses:
        if parenthesis == '(':
            stack.push(parenthesis)
        elif parenthesis == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
if __name__ == '__main__':
    examples = ['(()))','((()))','((()))']
    for example in examples:
        print(example + ': ' + str(balanced_parentheses(example)))
