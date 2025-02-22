                                                                         #PRINT
# print("Hello world")


#                                                                        #ADDITON AND DIVISION
# num1 = float(input("Enter the first number for addition"))
# num2 = float(input("Enter the second number for addition"))
# sum = num1 + num2
# print(f"{sum} {num1} + {num2} = {sum}")


# num3 = float(input("Enter the 3rd number for division"))
# num4 = float(input("Enter the 4th number for division"))
# if num4 == 0:
#    print("Error: division by zero is not allowed")
# else:
#     result = num3 / num4
# print(f"{result} num3 / num4 = {result}")
     
  
  
  
  
  
#                                                                               #AREA OF TRIANGLE
# base = float(input("Enter the length of the base of the triangle:"))
# hight = float(input("Enter the hight of the triangle:"))

# area = 0.5 * base * hight
# print(f"{area} {base} * {hight} = {area}")




#                                                                              # swap two variable
# a = input("Enter the value of the first variable:")
# b = input("Enter the value of the second variable:")   
# print(f"original value a = {a} , b = {b}")
# temp = b
# a = b
# b = temp
# print(f"swaped value a = {a} , b = {b}")
                                                                          

                                                                                 #random number

# import random
# print(f"Random number: {random.randint(1,100)}")

                                                                                  #kilometers to miles

# kilometers = float(input("Enter distance in kilometers: "))
# conversion_factor = 0.621371
# miles = kilometers * conversion_factor
# print(f"{kilometers} kilometers is equal to {miles} miles")


#                                                                                     #celsius to fahrenheit
# celsius = float(input("Enter temprature in celsius: "))       
# fahrenheit = (celsius * 9/5) + 32
# print(f"degree of celsius {celsius} is equal to degree of fahrenheit {fahrenheit}")               



                                                                                     #display calendar
# import calendar
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# cal =  calendar.month(year,month)
# print(cal)


                                                                                    #swap two variable without temp
# a = 5
# b = 10
# a ,b = b ,a
# print("After swaping")    
# print("a = ",a)   
# print("b = ",b)                                                                             



                                                                                #chk num + - or zero
# num = float(input("Enter a number: "))   
# if num > 0:
#     print("positive number")
# num = float(input("Enter a number"))  
# if num == 0:
#     print("zero")
# else:
#     print("negitive number")  



                                                                               #chk odd even
# num = int(input("Enter a number: "))  
# if num%2 == 0:
#     print("Even")  
# else:
#     print("odd")                                                                           


                                                                             #Leap year
# year = int(input("Enter a year"))   

# if(year % 400 == 0) and (year % 100 == 0): 
#    print("{0} is a leap year .format{year}: ")
# if (year % 4 == 0) and (year % 100 == 0):
#     print("{0} is leap year . format{year}: ")
# else:
#     print("{0} is not leap year . format{year}: ")
  
  
  
                                                                            #prime number
# num = int(input("Enter a number: "))
# flag = False
# if num == 1:
#  print(f"(num), is not a prime number")
# elif num > 1:
#   for i in range(2, num):
#    if (num % i) == 0:
#     flag = True 
#     break
#    if flag:

#     print(f"(num), is not a prime number")

# else:
#    print(f" (num), is a prime number")



                                                                                 #print all prime num
# lower = 1
# upper = 10
# print("Prime numbers between", lower, "and", upper, "are:")
# for num in range(lower, upper + 1):
#  if num > 1:
#   for i in range(2, num): 
#    if (num % i) == 0:
#      break
# else:
#  print(num)                        
 
 
 
                                                                               #factorial of a num
# num = int(input("Enter a number: "))
# factorial = 1
# if num <0:
#   print("Factirial does not exist for negative numbers")
# elif num == 0:
#  print("Factorial of 0 is 1")
# else:
#   for i in range(1, num+1):
#    factorial = factorial *i
# print(f'The factorial of (num) is {factorial}')                                                                              
 
 
                                                
                                                
                                                                                 #print table
# num = int(input("Display multiplication table of: "))

# for i in range(1, 11):
#   print(f"{num} X {i} = {num*i}")     

                                                                                                          
  
  
                                                                         #fabnocii sequance
# nterms = int(input("How many terms? "))
# n1, n2 = 0, 1
# count = 0
# if nterms <= 0:
#   print("Please enter a positive integer")
# elif nterms == 1:
#  print("Fibonacci sequence upto", nterms,":")
#  print(n1)
# else:
#  print("Fibonacci sequence:")
# while count <nterms:
#     print(n1)
#     nth= n1 + n2
#     n1 = n2
#     n2 = nth
#     count+= 1                                                     
                                                                                 #CHEK ARMSTRONG NUMBER 
# num = int(input("Enter a number: "))
# num_str = str(num)
# num_digits = len(num_str)
# sum_of_powers = 0
# temp_num = num
# while temp_num > 0:
                                                                                  #OUTPUT NOT CORRECT
#  digit =temp_num % 10
# sum_of_powers += digit ** num_digits
# temp_num //= 10
# if sum_of_powers == num:
#  print(f"(num) is an Armstrong number.")
# else:
#   print(f"{num} is not an Armstrong number.")



                                                                             #ARMSTRONG IS IMTERVAL
# num = int(input("Enter a number: "))
# num_str = str(num)
# num_digits = len(num_str)
# sum_of_powers = 0
# temp_num = num
# while temp_num > 0:
#  digit = temp_num % 10

# sum_of_powers += digit ** num_digits

# temp_num //= 10
# if sum_of_powers == num:
#  print(f"(num) is an Armstrong number.")

# else:
#  print(f"{num} is not an Armstrong number.")                                                                            
   
   
                                                                            #20sum of natural number

# lower = int(input("Enter the lower limit of the interval: "))
# upper = int(input("Enter the upper limit of the interval: "))
# for num in range(lower, upper + 1):
#  order = len(str(num)) #Find the number of digits in 'num'
# temp_num = num
# sum = 0
# while temp_num > 0:
#  digit = temp_num % 10
# sum += digit** order
# temp_num //= 10
# if num == sum:
#  print(num)                                                                            