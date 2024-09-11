import pdb
class Postfix:
    OPERATORS = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    def trim_white_space(expression):
        return expression.replace(" ","")
    
    def has_higher_precedence(a,b):
        if Postfix.OPERATORS[a] > Postfix.OPERATORS[b]:
            return True
        else:
            return False
    def has_equal_precedence(a,b):
        if Postfix.OPERATORS[a] == Postfix.OPERATORS[b]:
            return True
        else:
            return False
    
    def has_lower_precedence(a,b):
        if Postfix.OPERATORS[a] < Postfix.OPERATORS[b]:
            return True
        else:
            return False

    def convert_to_postfix(expression):
        #"a + b * c" == "a b c * +"
        expression = Postfix.trim_white_space(expression)
        sym_arr = []
        operator_arr =[]

        for char in expression:
            if char in Postfix.OPERATORS:
                operator_arr.append(char)
                if len(operator_arr) > 1:
                    for i in range(len(operator_arr)- 1):
                        if Postfix.has_higher_precedence(operator_arr[i],operator_arr[i+1]):
                            sym_arr.append(operator_arr.pop())
                        elif Postfix.has_equal_precedence(operator_arr[i],operator_arr[i+1]) and not operator_arr[i] == "^":
                            sym_arr.append(operator_arr[i])
                            operator_arr.remove(operator_arr[i])
            else:
                sym_arr.append(char)
        for i in range(len(operator_arr)):
            sym_arr.append(operator_arr.pop())
        return " ".join(sym_arr)

    def evaluate_to_postfix(self, expression = None):
        return None
    
    
  
        
    