import pandas as pd
import numpy as Np #or from numpy import * # These problems introduce data structures (lists, dictionaries, sets, tuples),
lst1 = [1,5,2,4,25,1,2123,23] # recursion, sorting, searching, and Pandas for data manipulation.
lst2 = [22,34,4,23,5,34,32,5]
lst3 = [1,2,3,4,5,6,7,8]

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverseFun(head):
    lowestvalue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < lowestvalue:
            lowestvalue = currentNode.data
        currentNode = currentNode.next
    print(lowestvalue)
    

    
node1 = Node(7)
node2 = Node(11)
node3 = Node(13)
node4 = Node(5)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseFun(node1)





# def findcommon(lst1,lst2):
#     commonlist = []
#     for i in lst1:
#         if i in lst2 and i not in commonlist:
#             commonlist.append(i)
#     return commonlist
# findcommon(lst1,lst2)


# a = Np.array([['Mon',12,14,18,11],['Tue',12,11,15,10]])
# print(a[0][0:3])

# b = Np.append(a,[['Wed', 14, 17, 21, 11]],0) # appends a new row at axis 0
# print(b)
# c = Np.insert(b,4,[[11,9,13 ]],1) # inserts a column for [available rows] on axis 1
# print(c)

# print(c.T)
# c = Np.delete(c,[5],1) #deletes index 5 elements of axis 1
# print(c)
# c = Np.delete(c,[0],0) #deletes row 0 from axis 0
# print(c)

# print(c.T)



# arr = [['one',1, 3, 4, 5],['two',2,5,5,22]]

# arr.insert(2, ['three',5,11,13,6])
# arr.insert(3, ['Four',2,4,1,4])

# arr[3][3] = 5
# #del arr[2]
# print(arr)


# def mergeSort(lst):


# def quickSort(lst):
#     if len(lst)<= 1:
#         return lst
#     #pivot = lst[len(lst)//2] #best case
#     pivot = lst[0]
#     # left = [x for x in lst if x < pivot]
#     # middle = [x for x in lst if x == pivot]
#     # right = [x for x in lst if x > pivot]

#     left = [x for x in lst[1:] if x <= pivot]
#     right = [x for x in lst[1:] if x > pivot]

#     #return quickSort(left) + middle + quickSort(right)
#     return quickSort(left) + [pivot] + quickSort(right)
# print(quickSort(lst3))


# def earlybubblesort(lst):
#     for i in range(len(lst)-1):
#         swapped = False
#         for j in range(len(lst)-i-1): # First pass i = 0 , inner loop swapped = True
#                                       # Second pass i = 1, if (inner loop swapped = Fasle) > break outer loop
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#                 swapped = True
#         if not swapped:
#                 break
                
#     return lst

# print(earlybubblesort(lst1))

# def bubblesort(lst):
#     for i in range(len(lst)-1): # len(lst)-1 is good option
#         for j in range(len(lst)-i-1): #why inside we access lst[j+1] which will be out of range
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     return lst

# print(bubblesort(lst1))

# def search(nums, target): # revesed sorted list
#     left, right = 0, len(nums) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if nums[mid] == target:
#             return mid

#         # Left half is sorted
#         if nums[left] <= nums[mid]:
#             if nums[left] <= target < nums[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         else:
#             # Right half is sorted
#             if nums[mid] < target <= nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#     return -1


# def searchInsert(nums, target): # expected index of target 
#         start = 0
#         last = len(nums)-1
#         while start <= last:
#             mid = (start+last)//2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid]<= target:
#                 start = mid+1
#             else:
#                 last = mid-1
#         return start
    
# print(searchInsert(lst2,34))


# def findElement(word, targetValue):
#     lst = sorted(word)
#     left = 0
#     right = len(lst)-1
#     while left <= right:
#         mid = (left+right)//2 #lst[mid] = 4 target = 25

#         if lst[mid] == targetValue:
#             return mid     
#         elif lst[mid] <= targetValue:
#             left = mid+1
#         else:
#             right = mid-1    

#     return "not found"

# print(findElement(lst1, 3))


# def longest_substring(word): #-----Try again
#     char_index = {}  # Track last index of each character
#     max_length = 0
#     max_substring = ""
#     start = 0
    
#     for end in range(len(word)):
#         # If character is seen and its last index is >= start, move start
#         if word[end] in char_index and char_index[word[end]] >= start:
#             start = char_index[word[end]] + 1
#         else:
#             # Update max_length and max_substring if current window is longer
#             if end - start + 1 > max_length:
#                 max_length = end - start + 1
#                 max_substring = word[start:end + 1]
        
#         # Update last seen index of current character
#         char_index[word[end]] = end
    
#     return max_substring


# print(longest_substring('LongestSubString'))




# def twoSum(lst, n):
#     for i in range(len(lst)):
#         a = lst[i] 
#         for j in range(i+1, len(lst)):
#             b = lst[j]
#             if a + b == n:
#                 return i, j #not - return lst.index[a], lst.index[b] error index[value] takes indices of first matched value

# print(twoSum(lst1, 2))
#-------------------------
# def twoSum(lst, n):
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i]+lst[j] == n:
#                 return i, j
# print(twoSum(lst1, 2))



# def validate_parentheses(value):
#     stack = []
#     for i in range(len(value)):
#         if value[i] == '(' or value[i] == '[' or value[i] == '{':
#             stack.append(value[i])
#         else:
#             if stack and ((stack[-1]=='(' and value[i] ==')') or
#                           (stack[-1]=='[' and value[i] ==']') or
#                           (stack[-1]=='{' and value[i] =='}')):
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0

# print(validate_parentheses('((('))



# def reverse_words(word):
#     new_string = ''
#     for i in word.split(' '):
#         new_string = i + ' ' + new_string
#     return new_string
# print(reverse_words("hello world"))


# def rotate_lst(lst):
#     k = 2
#     new_lst = lst[-k:]+lst[:-k]
#     return new_lst
# print(rotate_lst(lst1))
# #--------------------
# def rotate_lst(lst):
#     k = 2
#     new_lst = []

#     for i in range(1,k+1):
#         new_lst.append(lst[-i])
#     new_lst[:k] = new_lst[-k][::-1] #new_lst[start:end:step]

#     for j in range(len(lst)-k):
#         new_lst.append(lst[j])
#     return new_lst

# print(rotate_lst(lst1))


# def sorted_lst(lst1,lst2):
#     lst1 = sorted(lst1)
#     lst2 = sorted(lst2)
#     merged_lst = sorted(lst1+lst2)
#     return merged_lst
# print(sorted_lst(lst1,lst2))