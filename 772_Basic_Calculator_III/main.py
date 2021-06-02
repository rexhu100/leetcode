"""
Implement a basic calculator to evaluate a simple expression string. The expression string may contain open ( and
closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces . The expression string
contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The
integer division should truncate toward zero. You may assume that the given expression is always valid. All
intermediate results will be in the range of [ -2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
"""
from Solution import Solution


def calculate(s: str) -> int:
    s = "".join(s.split())
    prec = {"(": 1, "+": 2, "-": 2, "*": 3, "/":3}
    op_stack = []
    post_fix = []
    i = 0
    while i < len(s):
        if s[i].isnumeric():
            n = []
            while i < len(s) and s[i].isnumeric():
                n.append(s[i])
                i += 1
            post_fix.append("".join(n))
            continue
        elif s[i] == "(":
            op_stack.append("(")
        elif s[i] == ")":
            top_op = op_stack.pop()
            while top_op != "(":
                post_fix.append(top_op)
                top_op = op_stack.pop()
        else:
            # This part is for handling thing like +1+1, -3+2, 1+(-1), etc.
            if i - 1 < 0 or (i - 1 >= 0 and not s[i - 1].isnumeric() and s[i - 1] != ")"):
                post_fix.append("0")

            while len(op_stack) > 0 and prec[op_stack[-1]] >= prec[s[i]]:
                post_fix.append(op_stack.pop())
            op_stack.append(s[i])

        i += 1

    while len(op_stack) > 0:
        post_fix.append(op_stack.pop())

    num_stack = []
    for token in post_fix:
        if token.isnumeric():
            num_stack.append(int(token))
        else:
            n1 = num_stack.pop()
            n2 = num_stack.pop()
            if token == "+":
                num_stack.append(n1 + n2)
            elif token == "-":
                num_stack.append(n2 - n1)
            elif token == "*":
                num_stack.append(n1 * n2)
            elif token == "/":
                num_stack.append(n2 // n1)

    return num_stack.pop()


def main():
    sol = Solution()
    exp = "1 + 1"
    print(sol.calculate(exp))
    print(calculate(exp))

    exp = "(2+6* 3+5- (3*14/7+2)*5)+3"
    print(sol.calculate(exp))
    print(calculate(exp))

    exp = "2*(5+5*2)/3+(6/2+8)"
    print(sol.calculate(exp))
    print(calculate(exp))

    exp = "(-2 + 3) * 10 / 5 - 20*4"
    # print(sol.calculate(exp))  # Exception occurs... looks like mine is the real solution
    print(calculate(exp))


if __name__ == "__main__":
    main()

