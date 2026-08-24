class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
            elif tokens[i] == "+":
                x = stack.pop()
                y = stack.pop()
                z = int(y + x)
                stack.append(z)
            elif tokens[i] == "-":
                x = stack.pop()
                y = stack.pop()
                z = int(y - x)
                stack.append(z)
            elif tokens[i] == "*":
                x = stack.pop()
                y = stack.pop()
                z = int(y * x)
                stack.append(z)
            elif tokens[i] == "/":
                x = stack.pop()
                y = stack.pop()
                z = int(y / x)
                stack.append(z)
        
        return stack.pop()

        