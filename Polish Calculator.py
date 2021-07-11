# Write a small program that computes arithmetic expressions in postfix notation, also known as reverse
# polish notation or RPN.
# ● Use whichever language you want (advice: use the one you know best)
# ● Do it on your laptop in your favourite development environment.
# In postfix notation, parentheses and operator priorities are not necessary: an operator always applies to
# its immediately preceding arguments. For instance, consider the expression " 6 8 4 + 3 2 + - * ".
# ● The first operator "+" is applied to its preceding arguments, that is 8 and 4, giving 12. The sub-expression "8
# 4 +" is then replaced by its result 12, so the expression becomes " 6 12 3 2 + - * ".
# ● The next operator "+" is applied to its arguments, that is 3 and 2, giving 5. The sub-expression "3 2 +" is
# replaced by 5, so the expression becomes "6 12 5 - *".
# ● The next operator "-" is applied to its arguments, that is 12 and 5, giving 7. The sub-expression "12 5 -" is
# replaced by 7, so the expression becomes "6 7 *".
# ● The next operator "*" is applied to its arguments, that is 6 and 7, giving 42. The sub-expression "6 7 *" is
# replaced by 42, so the expression becomes "42".
# ● When all operators have been applied, the expression has become its result: 42.
# Your program must support the following operators:
# ● binary operators: + , - , * , /
# ● unary operator: sqrt (square root)
# Hint: One way to evaluate such expressions is to use a stack to store intermediate results.
# This can be a simple program in text mode, no need for a user interface. If you use Unix, you may get the
# input from the command-line arguments. Don’t handle input errors - assume it will be valid.

# Some examples: 3 4 2 + * gives 18 as result
# 5 4 2 * 3 + + sqrt gives 4 as result
# 3.12 4 + 2 * gives 14.24 as result

import operator
import math

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def solution(input_string):
    list1 = input_string.split()
    stack = []
    for item in list1:
        if item == '+' or item == '-' or item == '*' or item == '/':
            var1 = stack.pop()
            var2 = stack.pop()
            var3 = ops[item](var2,var1)
            stack.append(var3)
        elif item == 'sqrt':
            stack.append(math.sqrt(stack.pop()))
        else:
            stack.append(int(item))
    return stack

solution("5 4 2 * 3 + + sqrt")