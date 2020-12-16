import re
def arithmetic_arranger(problems, second_argument=False):

    line1, line2, line3, line4  = "", "", "", ""
    length=len(problems)
     
     
    for i, problem in enumerate(problems):
        operand1, operator, operand2 = problem.split()   

        if operand1.isdigit(): 
            pass

        elif operand2.isdigit(): 
            pass 
            
        if  not operand1.isdigit() : 
            return 'Error: Numbers must only contain digits.'       

        elif not operand2.isdigit()  :
            return 'Error: Numbers must only contain digits.'         
                 
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        if operator == '+' or operator == '-':
            pass

        if operator == '+':
            answer= str(int(operand1) + int(operand2))
             
        if operator== '-':
            answer= str(int(operand1) - int(operand2))  
          
        if len(operand1) > 4:
            return 'Error: Numbers cannot be more than four digits.'
            
        elif len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if len(operand1) < 4:
            pass
        if len(operand2) < 4:
            pass

        if length < 5:
            pass    

        if length > 5:
            return "Error: Too many problems."

        width = max(len(operand1),len(operand2)) 
        if i < length -1 :
            line1 += operand1.rjust(width+2)+" "*4
            line2 += operator + operand2.rjust(width+1)+" "*4
            line3 +=   '-' * (width+2)+" "*4 
            line4 += answer.rjust(width+2)+" "*4
        else:
            line1 += operand1.rjust(width+2)
            line2 += operator + operand2.rjust(width+1)
            line3 +=   '-' * (width+2)
            line4 += answer.rjust(width+2)
             

     
    if second_argument==True:
        return f"{line1}\n{line2}\n{line3}\n{line4}"
    elif second_argument==False:
        return f"{line1}\n{line2}\n{line3}"
   
   
   
    # reference: https://repl.it/@sasakr/01arithmeticarranger#main.py