# #contains duplicate
# def contains_duplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)
#     return False
# print(contains_duplicate([1, 2, 3, 4, 5]))  # Output: False
# print(contains_duplicate([1, 2, 3, 4, 5, 2]))  # Output: True

# #power four
# def is_power_of_four(n):
#     if n <= 0:
#         return False
#     while n % 4 == 0:
#         n //= 4
#     return n == 1

# #power of two
# def is_power_of_two(n):
#     if n <= 0:
#         return False
#     while n % 2 == 0:
#         n //= 2
#     return n == 1
# print(is_power_of_two(1))  # Output: True
# # #power of three
# # def is_power_of_three(n):
# #     if n <= 0:
# #         return False
# #     while n % 3 == 0:
# #         n //= 3
# #     return n == 1
# # print(is_power_of_three(27))  # Output: True
# # #power of four
# # def is_power_of_four(n):
# #     if n <= 0:
# #         return False
# #     while n % 4 == 0:
# #         n //= 4
# #     return n == 1
# # print(is_power_of_four(64))  # Output: True

# #best time to buy and sell stock
# # def max_profit(prices):
# #     min_price = float('inf')
# #     max_profit = 0
# #     for price in prices:
# #         if price < min_price:
# #             min_price = price

# #         elif price - min_price > max_profit:
# #             max_profit = price - min_price
# #     return max_profit
# # print(max_profit([7, 1, 5, 3, 6, 4]))  # Output: 5

# # # oops
# # class Car:
# #     def __init__(self, make, model, year):
# #         self.make = make
# #         self.model = model
# #         self.year = year

# #     def start_engine(self):
# #         return f"The {self.make} {self.model}'s engine has started."

# #     def stop_engine(self):
# #         return f"The {self.make} {self.model}'s engine has stopped."                                
# # my_car = Car("Toyota", "Camry", 2020)
# # print(my_car.start_engine())  # Output: The Toyota Camry's engine has started.            
# # print(my_car.stop_engine())   # Output: The Toyota Camry's engine has stopped.


# class student:
#     def __init__(self, name, mark):
#         self.name = name
#         self.mark = mark
#         if self.mark > 40:
#             print("This student is passed.")
#         else:
#             print("This student is failed.")
#             s1.details("rvs",80)
# #syntax
# class classname:
#     def method_name(self):
#         print("msg")
        
# # class student:
# #     def __init__(self, name, mark):
# #         self.name = name
# #         self.mark = mark
# #     def show_result(self):
# #         if self.mark > 40:
# #             print("This student is passed.")
# #         else:
# #             print("This student is failed.")
#            print("\n student ",self.name)
#            print("mark ",self.mark)
#            print("result ",result)
           
# name = input("enter name ")
# mark = int(input("enter mark "))
# s1 = student(name, mark)
# s1.show_result()

# #celcius to fahrenheit
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
# print(celsius_to_fahrenheit(25)) 

# encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance