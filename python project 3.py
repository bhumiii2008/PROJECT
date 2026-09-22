# #str ='I study in vit bhopal'
# #print(str)
# #print(str[1:6])
# #print(str[:7])
# a= int(input("Enter the first variable: "))
# b = int(input("Enter the second variable: "))
#
# print("Before swapping:")
# print("a =", a)
# print("b =", b)
#
# # Swap using tuple assignment
# a, b = b, a
#
# print("After swapping:")
# print("a =", a)
# print("b =", b)
#
# #salary
# def calculate_hra(basic):
#     return 0.20 * basic
#
# def calculate_da(basic):
#     return 0.10 * basic
#
# def calculate_gross_salary(basic):
#     hra = calculate_hra(basic)
#     da = calculate_da(basic)
#     return basic + hra + da
#
# # Input
# basic_salary = float(input("Enter basic salary: "))
#
# # Calculate
# hra = calculate_hra(basic_salary)
# da = calculate_da(basic_salary)
# gross_salary = calculate_gross_salary(basic_salary)
#
# # Output
# print("Basic Salary =", basic_salary)
# print("HRA =", hra)
# print("DA =", da)
# print("Gross Salary =", gross_salary)



# password = 789456
# attempt = 0
#
# while attempt < 3:
#     passcode = int(input("Enter the password: "))
#     attempt += 1
#
#     if passcode == password:
#         print("Correct password")
#         break
#     else:
#         print("Incorrect password")
#
# if attempt == 3 and passcode != password:
#     print("YOU HAVE LOST YOUR CHANCES")

        
username_valid = True
password_valid = True
otp_correct = True

if username_valid and password_valid and otp_correct:
    print("Access Granted")
else:
    print("Access Denied")


for i in range(1,102,2):
    print(i, end=" ")