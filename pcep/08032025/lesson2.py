#var = 1
#print(var)
#var = var + 1
#print(var)


#Grade = int(input("what is your grade in Class:"))
#if Grade >= 90:
 #   print("your grade is: A")
#elif Grade >= 80:
 #   print("Your grade is: B")
#elif Grade >= 70:
 #   print("your grade is: C")
#elif Grade >=60:
 #   print("your grade is: D")
#else:
#    print("Your grade is: F")




#Balance = float(input("what is your account balance: "))
#transaction1 = float(input(" first transaction: "))
#transaction2 = float(input("second transaction: "))
#transaction3 = float(input("third transaction: "))
#transaction4 = float(input("forth transaction: "))
#transaction5 = float(input("fifth transaction: "))
#total = transaction1 + transaction2 + transaction3 + transaction4 + transaction5
#print(total)
#if total < Balance:
#    print("your doing good")
#else:
#    print("you need to learn badgetting")

'''
program to check the balance '''

#Balance = float(input("What is your current balance?"))
#total_transaction = 0

#while total_transaction < Balance:
#    transaction = float(input("Enter your 1st transaction"))
#    total_transaction = total_transaction + transaction
#else:
#    print("you cant spend more")


'''
program to show grade and average
'''

'''
ask to input 5 students their zipcode
if zipcode is falls under 90034 then keep a count
program end
'''

zipcode=90034
zipcodecount = 0
student = 0

while student < 5:
    student_zipcode = int(input("Enter your zipcode"))
    if student_zipcode < zipcode:
        zipcodecount = zipcodecount + 1
    student = student + 1

else:
    print(zipcodecount "many students have same zipcode 90034")

   # student = int(input("What is your zipcode ?"))
    #student = student + 1


#zipcode = int(input("What is your zipcode= ?"))
#zipcode = 