class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = 0 
        prev_op = '+'
        s += '#'

        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c == '(':
                stack.append(prev_op)
                prev_op = '+'
            
            else:
                if prev_op == '+':
                    stack.append(cur)
                elif prev_op == '-':
                    stack.append(-1 * cur)
                elif prev_op == '*':
                    stack.append(stack.pop() * cur)
                else:
                    stack.append(int(stack.pop() / cur))
                
                cur = 0
                prev_op = c
                if c == ')':
                    while type(stack[-1]) == int:
                        cur += stack.pop()
                    prev_op = stack.pop()

        return sum(stack)