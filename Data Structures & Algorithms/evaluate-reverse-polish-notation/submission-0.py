class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for s in tokens:
            if s == "+":
                stack.append(stack.pop() + stack.pop())
            elif s == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif s == "*":
                stack.append(stack.pop() * stack.pop())
            elif s == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(float(a) / b))
            else:
                stack.append(int(s))
                
        return stack[0]
                