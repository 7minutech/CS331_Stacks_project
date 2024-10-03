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

    def convert_to_postfix(infix_expression):
        #"a + b * c" == "a b c * +"
        infix_expression = Postfix.trim_white_space(infix_expression)
        postfix_expression = []
        operators =[]
  
        for term in infix_expression:
            # need to add operands and operators to separate lists
            if term in Postfix.OPERATORS:
                operators.append(term)

                if len(operators) > 1:
                    for i in range(len(operators)- 1):
                        # only need to add to expression once one operator has higher precedence than another
                        # must exclude parenthesis
                        if Postfix.has_higher_precedence(operators[i],operators[i+1]) and not Postfix.OPERATORS[operators[i]] == 4:
                            postfix_expression.append(operators[i])
                            operators.remove(operators[i])
                        # need to check for parenthesis
                        # b/c operators enclosed with have highest precedence
                        if len(operators) > 2 and Postfix.is_enclosed_by_parenthesis(i,operators):
                            postfix_expression.append(operators[i])
                            for i in range(3):
                                operators.pop()
            # operands do not need to be checked 
            # before they are added to the expression
            else:
                postfix_expression.append(term)
        # any leftover operators can be added to the expression w/o checking
        for i in range(len(operators)):
            postfix_expression.append(operators.pop())
        return " ".join(postfix_expression)

    def evaluate_to_postfix(expression = None):
        """Calculate value"""
        stk = []
        nmbrs = ""
        if not expression:
            return 0
        if len(expression) == 1 and expression[0].isdigit():
            return int(expression)
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