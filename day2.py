# student_types = input("Enter the student type: ").lower()

# if student_types == "msh":
#     print("The student is a msh student")
#     tuition_fee = float(input("Enter the tuition fee: "))
#     hostel_fee = float(input("Enter the hostel fee: "))
#     total_fee = tuition_fee + hostel_fee
#     print("The fee to be paid by the student is $", total_fee)

# elif student_types == "msd":
#     print("The student is a msd student")
#     tuition_fee = float(input("Enter the tuition fee: "))
#     buss_fee = float(input("Enter the bus fee: "))
#     total_fee = tuition_fee + buss_fee
#     print("The fee to be paid by the student is $", total_fee)

# elif student_types == "mesd":
#     print("The student is a mesd student")
#     tuition_fee = float(input("Enter the tuition fee: "))
#     buss_fee = float(input("Enter the bus fee: "))
#     total_fee = tuition_fee + buss_fee
#     print("The fee to be paid by the student is $", total_fee)

# elif student_types == "mesh":
#     print("The student is a mesh student")
#     tuition_fee = float(input("Enter the tuition fee: "))
#     hostel_fee = float(input("Enter the hostel fee: "))
#     buss_fee = float(input("Enter the bus fee: "))
#     total_fee = tuition_fee + hostel_fee + buss_fee
#     print("The fee to be paid by the student is $", total_fee)

# else:
#     print("He/She is not a student type:", student_types)

# store_ballance=float(input("Enter the store balance: "))
# store_withdrawal=float(input("Enter the amount to withdraw: "))
# if store_withdrawal<=store_ballance:
#     new_balance=store_ballance-store_withdrawal
#     print("The new balance is $",new_balance)
# elif store_withdrawal>store_ballance:
#     print("The insufficient balance. You cannot withdraw $",store_withdrawal)
# elif store_withdrawal==store_ballance:
#     print("You have withdrawn all your money, Your new balance is $0")
# elif store_withdrawal>10000:
#     print("The withdrawal amount exceeds the limit. You cannot withdraw $",store_withdrawal)
# else:
#     print("Invalid input. Please enter a valid withdrawal amount.")

# account_balance=float(input("Enter the account balance: "))
# account_pin=int(input("Enter the account pin: "))
# if account_pin !=1234:
#     print("Pin is incorrect. You cannot proceed with your transaction.")
#     if account_pin==1234:
#         print("Pin is correct. You can proceed with your transaction.")
#         withdrawal_amount=float(input("Enter the amount to withdraw: "))
#         if withdrawal_amount<=account_balance:
#             new_balance=account_balance-withdrawal_amount
#             print("The new balance is $",new_balance)
#         elif withdrawal_amount>account_balance:
#             print("The insufficient balance. You cannot withdraw $",withdrawal_amount)
#         elif withdrawal_amount==account_balance:
#             print("You have withdrawn all your money, Your new balance is $0")
#         elif withdrawal_amount>10000:
#             print("The withdrawal amount exceeds the limit. You cannot withdraw $",withdrawal_amount)
#         else:
#             print("Invalid input. Please enter a valid withdrawal amount.")

# age=int(input("Enter your age: "))
# child=150
# adult=250
# senior=200
# if age<18:
#     print("The ticket price for child is$",child)
# elif age>=18 and age<60:
#     print("The ticket price for adult is $",adult)
# elif age>=60:
#     print("The ticket price for senior is $",senior)
# else:
#     print("deadman")
# show_time=str(input("Enter the show time (morning/evening): ").lower())
# if show_time=="morning":

#     if age<18:
#         print("The ticket price for child is $",child-50)
#     elif age>=18 and age<60:
#         print("The ticket price for adult is $",adult-50)
#     elif age>=60:
#         print("The ticket price for senior is $",senior-50)
#     else:
#         print("deadman")
# elif show_time=="evening":
#     if age<18:
#         print("The ticket price for child is $",child)
#     elif age>=18 and age<60:
#         print("The ticket price for adult is $",adult)
#     elif age>=60:
#         print("The ticket price for senior is $",senior)
#     else:
#         print("deadman")
# else:
#     print("Invalid show time. Please enter 'morning' or 'evening'.")

# loop
# sum=0
# for i in range (1,100):
#     odd_number=i%2
#     if odd_number==1:
#         print(i)
#         sum=sum+i
# total=sum
# print("The total of odd numbers is",total)

# sum=0
# for i in range(1,100):
#     if i%2==0:
#         sum=sum+i
#         print(i)
# print("The total of even numbers is",sum)

# for i in range(1,11):
#     sum=i*5
#     print(i,"* 5 =",sum)

# n=5
# for i in range(1,n+1):
#     print("$"*i)

# n=5
# for i in range(n,0,-1):
#     print("*"*i)
# sum=0
# i = 1
# while i <= 100:
#     if i % 2 == 1:
#         print(i)
#         sum += i
#     i += 1
# print("The total of odd numbers is", sum)

# sum=0
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         print(i)
#         sum += i
#     i += 1
# print("The total of even numbers is", sum)

# i=1
# while i <= 5:
#     print("*"*i)
#     i += 1

# i=5
# while i >= 0:
#     print("*"*i)
#     i -= 1

# i=1
# while i <=10:
#     sum=i*5
#     print(i,"*5 =",sum)
#     i += 1

availble_seats=int(input("Enter the number of available seats: "))
while availble_seats > 0:
    print("There are", availble_seats, "seats available.")
    seats_to_book = int(input("Enter the number of seats to book: "))
    passanger_name = input("Enter the passenger name: ")  
    if seats_to_book <= availble_seats:
        availble_seats -= seats_to_book
        print("You have successfully booked", seats_to_book, "seats.")
    else:
        print("Sorry, there are only", availble_seats, "seats available. Please try again.")