#Making a calculator
from art import logo

#Addition
def add(n1, n2):
  return n1 + n2
#Subtraction
def subtract(n1, n2):
  return n1 - n2
#Multiplication
def multiply(n1, n2):
  return n1 * n2
#Division
def divide(n1, n2):
  return n1 / n2
#Types of operations
operations_dict = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
#Main calculator function
def calculator():
  print(logo)
  num1 = input("Enter the first number: ")
  
  print("........................")
  for symbol in operations_dict:
    print(symbol)
  print("........................")
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Please pick an operation: ")
    num2 = input("Enter the next number: ")
  
    calculation_function = operations_dict[operation_symbol]
    output = round(calculation_function(float(num1), float(num2)),2)
    print(f"{num1} {operation_symbol} {num2} = {output}")
  
    go_next = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
    if go_next == 'y':
      num1 = output
    else:
      should_continue = False
      calculator()

calculator()
