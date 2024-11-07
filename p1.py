class Stack():
    def __init__(self):
        self.storage = []

    def push(self, newValue):
        self.storage.append(newValue)

    def top(self):
        return self.storage[len(self.storage) - 1]

    def pop(self):
        result = self.top()
        self.storage.pop()
        return result

    def isEmpty(self):
        return len(self.storage) == 0


class CalculatorEngine():
    def __init__(self):
        self.dataStack = Stack()

    def pushOperand(self, value):
        self.dataStack.push(value)

    def currentOperand(self):
        return self.dataStack.top()

    def performBinaryOp(self, fun):
        right = self.dataStack.pop()
        left = self.dataStack.pop()
        self.dataStack.push(fun(left, right))

    def doAddition(self):
        self.performBinaryOp(lambda x, y: x + y)

    def doSubtraction(self):
        self.performBinaryOp(lambda x, y: x - y)

    def doMultiplication(self):
        self.performBinaryOp(lambda x, y: x * y)

    def doDivision(self):
        try:
            self.performBinaryOp(lambda x, y: x / y)
        except ZeroDivisionError:
            print("divide by 0!")
            exit(1)
        
    def doModulo(self):
        try:
            # your code here
        except # your code here
            print("divide by 0!")
            exit(1)


    def doTextOp(self, op):
        if (op == '+'):
            self.doAddition()
        elif (op == '-'):
            self.doSubtraction()
        elif (op == '*'):
            self.doMultiplication()
        elif (op == '/'):
            self.doDivision()
        elif (op == '%'):   # don't update CalcEngine here
            self.doModulo()


class RPNCalculator(CalculatorEngine):
    def __init__(self):
        # your code here

    def eval(self, line):
        # your code here

    def run(self):
        while True:
            line = input("type an expression: ")
            if len(line) == 0:
                break
            print(self.eval(line))

if __name__ == '__main__':
    cal = RPNCalculator()
    cal.run()
