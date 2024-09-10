class Postfix:
    OPERATORS = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    def __init__(self,expression = None):
        self.expression = expression

    def convert_to_postfix(self, expression = None):
        #"a + b * c" == "a b c * +"
        if self.expression is not None:
            print("case 1")
        elif expression is not None:
            print("case 2")
        else:
            print("case 3")
    def evaluate_to_postfix(self, expression = None):
        return None
    
    def set_expression(self, expression):
        self.expression = expression

    def set_operand_arr(self):
        operand_arr = []
        for char in self.expression:
            if char not in self.OPERATORS:
                operand_arr.append(char)
        return operand_arr



