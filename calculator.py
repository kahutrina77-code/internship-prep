def calculate(num1, num2, operator):
   if operator ==  "+" :
      return num1 + num2 

   elif operator == "-" :
       return num1 - num2

   elif operator == "*" :
      return num1 * num2
   
   elif operator == "/" :
      if num2 == 0 :
         return "Error"
      return num1 / num2 

   else :
      return "Uknown operator"

running = True

while running:
   num1 = float(input("first number: "))
   num2 = float(input("second number: "))
   operator = input("Enter operator(+,-,/,*): ")

   result = calculate(num1, num2, operator)   

   print(result)

   again = input("calculate again(Y/n):")
   if again != "Y" :
      running = False

print("Bye!")



