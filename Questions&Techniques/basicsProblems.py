
# lst = [1,12,1,2,13,1,41]
# list comprehension, enumerate(lst)
#---------
# def delete(lst):
#     newlst = []
#     for i in lst:
#         if i not in newlst:
#             newlst.append(i)
#     return newlst

# print(delete([1,12,1,2,13,1,41]))

# from collections import Counter # Best method like count use Counter
# lst = [1,2,32,1,3,2,12,1,2,2]
# dictionary = Counter(lst)

# print(dictionary)
#----------------
#//old method
# def occurrence(lst):
#     count_dict = {}
#     for item in lst:
#         if item in count_dict:
#             count_dict[item] += 1
#         else:
#             count_dict[item] = 1
#     return count_dict

# print(occurrence([1,2,32,1,3,2,12,1,2,2]))



# def secondLargest(lst): #best case
#     if len(lst)<2:
#         return ValueError("List should have two elements atleast")
#     sorted_list = sorted(lst, reverse = True)
#     return sorted_list[1]

# my_list = [1,13,4,12, 11]
# print(secondLargest(my_list))

    

# def fibonacci(num):
#     a = 1
#     b = 1
#     series = [a, b]
#     for i in range(num - 2):
#         a = a + b
#         b = b + a
#         series += [a, b]
#     return series[:num] #inital return series[] but series[:num] works for odd numbers > range(1, int((num+1)/2))

# print(fibonacci(5))



# def palindrome(word):
#     reverse = ''
#     for i in word :
#         reverse = i + reverse
#     #return reverse == word

# print(palindrome('racecar'))
        

# def sumOfElements(my_list):
#     value = 0
#     for i in my_list[:]:
#         value += i
#     return value

# my_list = [5, 12,24, 43, 2]   
# print(sumOfElements(my_list))    # NOT good practice print(sumOfElements([5, 12, 24, 43, 2]))


# def maximumNum(my_list):
#     num = my_list[0]     # intial use num = 0, tip from GPT (num = my_list[0])
#     for i in my_list[:]:
#         if num < i:
#             num = i 

#     return num
# my_list = [ -10, -3, - 13]
# print(maximumNum(my_list))


# def countVowels(string):
#     value = 0
#     for i in string.lower():
#         if i in ['a','e','i','o','u']:
#             value = value + 1
#     return value

# print(countVowels('afgwerthyeeeervsbnh'))



# def reverseFun(letter):
#     reverse = ''
#     for i in letter:
#         reverse = i + reverse
#     return reverse

# print(reverseFun("hello"))



# def checkprime(num):
#     if num < 2:   # 0, 1 not prime numbers
#         return print('not a prime number')
#     for i in range(2, int(num**0.5) + 1):     # why not num/2? (Also correct)  36 = 6*6 NO tWO FACTORS ARE GREATER THAN SQUARE ROOT ex: 18*2
#         if num % i == 0:
#             return print('not a prime number')
#     return print('prime number')


# checkprime(7)



# a = 2;b = 3
# b = b + a
# a = b - a
# b = b - a
# print(a,b)
# c = 3;d = 5
# c,d = d,c
# print(c,d)

# def factorial(num):
#     fact = 1
#     i = 1
#     if num > 0:
#         while i <= num:
#             fact = fact * i
#             i += 1
#         return fact
    
# print(factorial(5))

      
# def checkInt(num):
#     if num % 2 == 0:
#         print("Given num is even")
#     else:
#         print("Given num is Odd")

# checkInt(10)


# a = 10
# b = 20
# def adding( x, y):
#     sum = x + y
#     return sum
# print(adding(a,b))