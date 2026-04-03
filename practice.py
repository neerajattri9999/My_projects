# Sorting 
'''
import random
import string
li=[]
for i in range(0,6):
    n=random.randint(30,100)
    li.append(n)
print(f"original string is {li}")
for i in range(0, len(li)):
    for j in range(i+1, len(li)):
        if li[i]>=li[j]:
            li[i], li[j]=li[j], li[i]
print("sorted list", li)

'''


#reversing a string


'''
def reverse_string(s):
    reversed_s = ""
    for i in range(len(s) - 1, -1, -1):  
        reversed_s += s[i]
    return reversed_s 
'''

'''
len(s) - 1 - This expression calculates the index of the last character in the string s. Since Python uses 0-based indexing, the length of the string minus 1 gives the index of the last character.
-1 - This is the stopping condition for the loop. It means that the loop will continue until it reaches index -1 (which is just before the first character in the string).
-1 - This is the step value for the loop. 
'''

'''
# Input string
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Generate a random string of length 10
input_string = generate_random_string(10)
print("Generated string:"+ " " +input_string)

# Reversing the string
reversed_string = reverse_string(input_string)

# Output
print("Original string:", input_string)
print("Reversed string:", reversed_string)

''' 

# Longest common seubsequence\
'''

def LCS(X, Y, m, n):
    if m == 0 or n == 0 :
        return 0,""  #returning multiple values from a function
    elif X[m-1] == Y[n-1]:
        length, subsequence=LCS(X, Y, m-1, n-1)
        return length + 1, subsequence + Y[n-1]
    else:
        length1, subsequence1=LCS(X, Y, m-1, n)
        length2, subsequence2=LCS(X, Y, m, n-1)
        if length1 > length2:
            return length1, subsequence1
        else:
            return length2, subsequence2

X="AGGTAB"
Y="GXTXAYB"
length, subsequence = LCS(X, Y, len(X), len(Y))
print(f"LCS is {subsequence} with length {length}")

'''

'''
# reverse a string
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
s = "Geeksforgeeks"
 
print("The original string is : ", end="")
print(s)


 
print("The reversed string(using loops) is : ", end="")
print(reverse(s))
'''





'''
# Counting Vowels in a Given Word
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)
'''

'''
#Writing Fibonacci Series
fib = [0,1]
# Range starts from 0 by default
for i in range(5):  
    fib.append(fib[-1] + fib[-2]) 

# Converting the list of integers to string
print(', '.join(str(e) for e in fib))
'''

'''
#Factorial 
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Test the function
number = 5
print(f"The factorial of {number} (recursive) is: {factorial_recursive(number)}")
'''


# li=[1,2,3,4,5,6]
# li.remove(4)
# li.pop(1)
# li


# import numpy as np
# import matplotlib.pyplot as plt
# x=np.linspace(1,50,50)
# np.random.seed(1)
# y=np.random.randint(0,20,50)
# plt.plot(x,y)
# plt.legend(['Legend'], loc='upper left')
# plt.show()




# import numpy as np
# import matplotlib.pyplot as plt
# plt.figure(figsize=(4,2))
# plt.title("name and experience graph")
# x=['Arjun','Bharat','Raju','Seeta', 'Ram']
# y=[5,7,8,4,6]
# plt.bar(x,y,color='g')
# plt.xlabel('Students', fontsize=10)
# plt.ylabel('Marks', fontsize=10)
# plt.legend(['Marks Scored'], fontsize=10,loc='upper right')
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[3,3,3,3,3]
# plt.plot(x,y, label='line-1')
# plt.plot(y,x, label='line-2')
# plt.plot(x,np.sin(x), label='curve-1')
# plt.plot(x,np.cos(x), label='curve-2')
# plt.title('line and curve')
# plt.legend(labelspacing=1)
# plt.show()




# import numpy as np 
# import matplotlib.pyplot as plt
# plt.plot([0,3],[0,2.0], label='label 1')
# plt.plot([0,3],[0,2.1], label='label 2')
# plt.plot([0,3],[0,2.2], label='label 3')
# plt.plot([0,3],[0,2.3], label='label 4') 
# plt.legend(ncol=3)
# plt.show()


# a,b,c,d=map(int, input())
# print(a,b,c,d)





# a,b,c=map(int, input().split(","))
# print(a+b+c)


# def remove_duplicates(nums):
#     unique_numbers = []
#     for num in nums:
#         if num not in unique_numbers:
#             unique_numbers.append(num)
#     return unique_numbers

# # Test the function
# nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
# unique_nums = remove_duplicates(nums)
# print(unique_nums)






# def bubble_sort(elements):
#     n = len(elements)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if elements[j] > elements[j + 1]:
#                 elements[j], elements[j + 1] = elements[j + 1], elements[j]

# # Test the function
# nums = [5, 2, 8, 1, 9]
# bubble_sort(nums)
# print(nums)



# #removing dupli and sort 

# def remove_dupli_and_sort(li):
#     updated_li=[]
#     for i in li:
#         if i not in updated_li:
#             updated_li.append(i)
    
#     for i in range(0,len(updated_li)-1):
#         for j in range(len(updated_li)-i-1):
#             if updated_li[j]> updated_li[j+1]:
#                 updated_li[j], updated_li[j+1] = updated_li[j+1], updated_li[j]
#     return updated_li
# li=[34,3,3,4,5,33,4,5,67,6,77,88,76,44,33]
# updated=remove_dupli_and_sort(li)
# print(updated)



## count common elements
# def counted(l1,l2):
#     counted_li=[]
#     for i in l1:
#         if i in l2:
#             counted_li.append(i)
#     return counted_li
# l1=[1,2,3,4,5,6,7]
# l2=[4,5,6,7,8,9]
# count=counted(l1,l2)
# print(count)

# li=[1,2,3,4,5,6]
# print(li[::-1])



# def largest(li):
#     large=li[0]
#     for i in li:
#         if i>large:
#             large=i
#     return large



# li=[4,3,2,6,7,5,64,33,22,54]
# lar=largest(li)
# print(lar)


# import numpy as np
# arr1=np.array([1,2,3,4])
# arr2=np.flip(arr1)
# print(arr2)


# import numpy as np
# arr1=np.array([1,2,3,4])
# arr2=np.delete(arr1,2)
# print(arr2)


# l1=[1,2,3,4]
# l2=[5,6,7,8]
# l3=[x+y for x,y in zip(l1,l2)]
# print(l3)



import pandas as pd
df=pd.read_csv(r'C:/Users/nsatt/OneDrive/Desktop/file.csv')
df.columns


python venv Ravi_env
Ravi_env/scripts/activate 


