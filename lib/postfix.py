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
                            elif self.OPERATORS[operator_arr[i]] == self.OPERATORS[operator_arr[i+1]] and operator_arr[i] != "^":
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
    def evaluate_to_postfix(expression = None):
        """Calculate value"""
        stk = []
        nmbrs = ""
        for element in expression:
           
            if element.isdigit():
                nmbrs += element
            elif element == " " and len(nmbrs) >= 1:
                stk.append(int(nmbrs))
                nmbrs = ""
            elif element != " ":
                two = stk.pop()
                one = stk.pop()
                result = 0
                if element == "-":
                    result = one-two
                elif element == "+":
                    result = one+two
                elif element == "/":
                    result = one/two
                elif element == "*":
                    result = one*two
                elif element == "^":
                    result = pow(one,two)
                stk.append(result)
            
        return stk[0]
    
    def set_expression(self, expression):
        self.expression = expression
