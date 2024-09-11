import pdb
class Postfix:
    OPERATORS = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": 4, ")": 4}

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
    
    def is_enclosed_by_parenthesis(index, arr):
        if arr[index-1] == "(" and arr[index+1] == ")":
            return True
        else:
            return False
        
    def is_set_of_parenthesis(char):
        if char == "(":
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
                        if Postfix.has_higher_precedence(operator_arr[i],operator_arr[i+1]) and not operator_arr[i] == "(" or operator_arr[i] == ")":
                            sym_arr.append(operator_arr[i])
                            operator_arr.remove(operator_arr[i])

                        elif Postfix.has_equal_precedence(operator_arr[i],operator_arr[i+1]) and not operator_arr[i] == "^":
                            sym_arr.append(operator_arr[i])
                            operator_arr.remove(operator_arr[i])
                        if len(operator_arr) > 2 and Postfix.is_enclosed_by_parenthesis(i,operator_arr):
                            sym_arr.append(operator_arr[i])
                            operator_arr.remove(operator_arr[i+1])
                            operator_arr.remove(operator_arr[i])
                            operator_arr.remove(operator_arr[i-1])
                            

            else:
                sym_arr.append(char)
        for i in range(len(operator_arr)):
            sym_arr.append(operator_arr.pop())
        return " ".join(sym_arr)

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
    
    
  
        
    