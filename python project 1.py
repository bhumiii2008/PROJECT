#wap to check if two tuples are same or not
#tuple1= (1,3,4,5,6,7,8)
#tuple2= (1,3,4,5,6,7,8)
#if(tuple1==tuple2):
   # print("Tuples are same")
#else:
    #print("Tuples are not same")

#WAP to navigate elements in the list
#list1=['apple','banana','cherry','kiwi']
#for element in list1:
    #print(element)

#Calling function
#def diff(a,b):
  # return a-b
#a=89
#b=45
#peration = diff
#print(operation(a,b))


#global and local variable 
#num1=10
#print('global variable=',num1)
#def func(num2):
 #   print("in function the local variable=",num2)
#num3=30
#print("local variable=",num3)
#func(20)
#print("num1 again",num1)
#print("num 3again",num3)

#sum = 0

#for i in range(1, 71):
 #   sum = sum + i

#print("Sum of first 70 natural numbers =", sum)


#a=2
#b=3
#c=a+b
#print(c)
#print(type(c))

#i = {"Name": "Bhumika", "Age": 18} 
#print(i) 
#print(type(i))

#print("\a")



#from math import sqrt
#num=16
#print(sqrt(num))

#from math import pow
#num1=2
#num2=6
#print(pow(num1,num2))

#a=63.8
#print(type(a))



#employee = input("Are you an employee? (yes/no): ")

#if employee == "no":
  #  print("No Access")
#else:
    #department = input("Enter your department: ")

    #if department == "IT" or department == "HR":
     #   print("Full Access")
    #else:
     #   print("Limited Access")
def reverse_string():
    s = input("Enter a string: ")
    print("Reverse =", s[::-1])


reverse_string()