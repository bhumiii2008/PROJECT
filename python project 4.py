#SWAPPING
#a= 10
#b= 20
#print(a)
#print(b)
#a, b = b, a
#print("After swapping")
#print(a)
#print(b)


##SWAPPING USING THIRD VARIABLE
#a=10
#b=50
#print(a)
#print(b)
#c=a
#a=b
#b=c
#print("After swapping")
#print(a)
#print(b)


##SWAPPING USING XOR
#x=10
#y=20
#print(x)
#print(y)
#x = x ^ y;
#y = x ^ y;
#x = x ^ y;
#print("After swapping")
#print(x)
#print(y)


#COUNTING DIGITS IN THE GIVEN NUMBER
#num=int(input("Enter number: "))
#count = 0
#while num > 0:
 #   count += 1
  #  num //= 10
#print("Number of digits:", count)

#RECURSIVE FUNCTION TO COUNT DIGITS
#def count_digits(n):
    #if n==0:
   #     return 0
    #else:
     #   return 1 + count_digits(n//10)
#n=int(input("Enter the number: "))
#print("Number of digits:",count_digits(n))



#AVERAGE AND SUM OF N NUMBERS
#n=int(input("Enter the number fo elements:"))
#sum=0
#for i in range(0,n+1,1):
 #   sum=sum+i
#average=sum/n
#print("Sum of n numbers",sum)
#print("Average of n numbers",average)


#SUM OF N NUMBERS USING FORMULA
#n=int(input("Enter the number of elements:"))
#sum = n*(n+1)/2
#average = sum/n
#print ("Sum of n mumbers",sum)
#print("average of n numbers",average)
 

#SUM AND AVERAGE OF N NUMBERS INPUT BY THE USER
# numbers=input("Enter numbers separated by spaces")
# numberList=numbers.split()

# print("\n")
# print("Then numbers in the number list are",numberList)

# sum1=0
# for i in numberList:
#     sum1=sum1+int(i)
# average=sum1/len(numberList)
# print("the sum is",sum1)
# print("average is",average)



#multiple number sum 
#sum=0
#num=[11,22,33,44,55,66,77]
#for i in num:
#    sum=sum+i
#    ave=sum/len(num)
#print("The sum is ",sum)
#print("The average is ",ave)



#FIBBONACCI SERIES
#n=int(input("enter the number of terms"))
#if n<2:
#    print("enter number greater than 2")
#else:
#    N1=0
#    N2=1
#    i=0
#print(N1,N2,end=" ")
#N3=N1+N2
#while i<n:
#    print(N3,end=" ")
#    N1=N2
#    N2=N3
#    N3=N1+N2
#    i=i+1



#REVERSE THE DIGITS
#digit=int(input("Enter the number"))
#reverse=0
#while digit>0:
#    reverse=reverse*10
#    reverse=reverse+digit%10
#    digit=digit//10
#print("The reverse of the number is", reverse)




#DECIMAL TO ANY BASE
#decimal=int(input("Enter the decimal number"))
#base=int(input("enter the base(2to 128)"))
#digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrsuvwxyz!@#$%^&*()_+{}"
#results=" "
#
#if decimal==0:
#    results="0"
#else:
#    while decimal>0:
#        remainder=decimal%base
#        results=digits[remainder]+results
#        decimal=decimal//base
#print("The number in base",base,"is",results)



#age=int(input("Enter your age:"))
#if(age>18):
#    print("Eligible to vote")
#else:
#    yrs=18-age
#    print("You have to wait for another "+str(yrs)+" years to vote")



#password=789456
#passcode=int(input("Enter the passcode"))
#if(passcode==password):
 # print("correct passcode")
#else:
 # print("incorrect passcode") 



# num=int(input("Enter any number from 0 to 30 ="))
# if(num>=0 and num<10):
#   print("The number is in the range of 0-10")
# elif(num>=10 and num<20):
#   print("The number is in the range of 10-20")
# elif(num>=20 and num<30):
#   print("The number is in the range of 20-30")





# def calculate(marks):
#     total = sum(marks)
#     percentage = total / 5
#     return total, percentage
#
# marks = [80, 75, 90, 85, 70]
#
# total, percentage = calculate(marks)
#
# print("Total marks =", total)
# print("Percentage =", percentage)




# for i in range(5):
#      print()
#      for j in range(4):
#       print("*" ,end=" ")



#i=1
#while i<=10:
# print(i,end=" ")
# if(i==5):
#    break  
# i=i+1
#print("\n Done")



#for i in range(1,11):
#    if(i==5):
#        continue
#    print(i,end=" ")
#print("\n Done")



#for letter in "HELLO":
 #   pass
 #   print("Pass:",letter)
#print("done")



