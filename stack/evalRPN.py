def evalRPN(tokens):
        res = []
        for i in range(len(tokens)):
            
            if tokens[i] == "+":
                updateToken = res.pop() + res.pop()
                res.append(updateToken)
            elif tokens[i] == "*":
                updateToken = res.pop() * res.pop()
                res.append(updateToken)

            elif tokens[i] == "/":
                firstInt = res.pop()
                secondInt = res.pop()
                updateToken = int(secondInt / firstInt)
                res.append(updateToken)
            elif tokens[i] == "-":
                firstInt = res.pop()
                secondInt = res.pop()
                updateToken = secondInt - firstInt
                res.append(updateToken)
            else:
                res.append(int(tokens[i]))
            print(res)
        return res.pop()
