class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c.isnumeric():
                stack.append(int(c))
            else:
                if c != '*' and c!= '/' and c!= '+' and c!= '-':
                    stack.append(int(c))
                else:
                    val2 = stack.pop()
                    val1 = stack.pop()
                    match c:
                        case '*':
                            stack.append(val1*val2)
                        case '-':
                            stack.append(val1-val2)
                        case '+':
                            stack.append(val1+val2)
                        case '/':
                            stack.append(int(val1/val2))
        return int(stack[-1])

