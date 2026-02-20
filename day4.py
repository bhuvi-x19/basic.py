# palindrome
# a=input("Enter a string: ")
# if a==a[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# a=input("Enter a string: ")
# rev=""
# for ch in a:
#     rev=ch+rev
#     if a==rev:
#         print("The string is a palindrome.")
#     else:
#         print("The string is not a palindrome.")

# num = int(input("Enter a number: "))
# if num == 0:
#     print(0)
# else:
#     print(1 + (num - 1) % 9)
# a=[1,2,3,4,5]
# a.sort(reverse=True)
# print(a)

# s = input("Enter first string: ")
# l = input("Enter second string: ")

# def is_anagram(s, l):
#     if len(s) != len(l):
#         return False
#     return sorted(s) == sorted(l)
# if is_anagram(s, l):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")

#climbing stairs
# n=int(input("Enter the number of stairs: "))
# if n!=0:
#     if n==1:
#         print(n)
#         if n==2:
#             print(n)
#             dp=[1]*n
#             dp[1]=2
#             for i in range(2,n):
#                 dp[i]=dp[i-1]+dp[i-2]
#             print(dp[n-1])
# print("no steps to climb")

#length of last word
# s=input("Enter a string: ")
# def length_of_last_word(s):
#     words=s.split()
#     if len(words)==0:
#         return 0
#     else:
#         return len(words[-1])
# print("The length of the last word is",length_of_last_word(s))

#intersection of two arrays
# a=[1,2,3,4,5]
# b=[4,5,6,7,8]
# def intersection(a,b):
#     set_a=set(a)
#     set_b=set(b)
#     return list(set_a & set_b)
# print("The intersection of the two arrays is",intersection(a,b))

# union of two arrays
# a=[1,2,3,4,5]
# b=[4,5,6,7,8]
# def union(a,b):
#     set_a=set(a)
#     set_b=set(b)
#     return list(set_a | set_b)
# print("The union of the two arrays is",union(a,b))

#intersection of two arrays
# a=[1,2,3,4,5]
# b=[4,5,6,7,8]
# def intersection(a,b):
#     set_a=set(a)
#     set_b=set(b)
#     return list(set_a & set_b)
# print("The intersection of the two arrays is",intersection(a,b))

#merege two sorted lists
# a=[1,3,5,7,9]
# b=[2,4,6,8,10]
# def merge_sorted_lists(a,b):
#     merged_list=a+b
#     merged_list.sort()
#     return merged_list
# print("The merged sorted list is",merge_sorted_lists(a,b))

#reverse string
# s=input("Enter a string: ")
# def reverse_string(s):
#     rev=""
#     for ch in s:
#         rev=ch+rev
#     return rev
# print("The reversed string is",reverse_string(s))

# num = int(input("Enter a number: "))
# if num == 0:
#     print(0)
# else:
#     print(1 + (num - 1) % 9)

# move zeroes
# a=[0,1,0,3,12]
# def move_zeroes(a):
#     non_zeroes=[x for x in a if x!=0]
#     zeroes=[x for x in a if x==0]
#     return non_zeroes+zeroes
# print("The array after moving zeroes is",move_zeroes(a))

