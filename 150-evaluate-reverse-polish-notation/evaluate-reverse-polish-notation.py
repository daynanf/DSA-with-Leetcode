class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif x == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif x == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif x == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b)) 
            else:
                stack.append(int(x))
        return stack[0]