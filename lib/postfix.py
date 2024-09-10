import pdb
class Postfix:
    OPERATORS = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    def __init__(self,expression = None):
        self.expression = expression.replace(" ","")

    def convert_to_postfix(self, expression = None):
        #"a + b * c" == "a b c * +"
        sym_arr = []
        operator_arr =[]
        if self.expression is not None:
            for char in self.expression:
                if char in self.OPERATORS:
                    operator_arr.append(char)
                    if len(operator_arr) > 1:
                        for i in range(len(operator_arr)- 1):
                            if self.OPERATORS[operator_arr[i]] > self.OPERATORS[operator_arr[i+1]]:
                                sym_arr.append(operator_arr.pop())
                            elif self.OPERATORS[operator_arr[i]] == self.OPERATORS[operator_arr[i+1]]:
                                sym_arr.append(operator_arr[i])
                                operator_arr.remove(operator_arr[i])

                else:
                    sym_arr.append(char)
            for i in range(len(operator_arr)):
                sym_arr.append(operator_arr.pop())
            return " ".join(sym_arr)

        elif expression is not None:
            print("case 2")
        else:
            print("case 3")
    def evaluate_to_postfix(self, expression = None):
        return None
    
    def set_expression(self, expression):
        self.expression = expression
