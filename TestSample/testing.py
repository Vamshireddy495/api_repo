import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = arr1[::-1]
print(arr2)
# import os
# os.remove('Lists.py')

# terinary operator score = 75
# print('Fail' if score < 50 else 'Merit' if score < 70 else 'Distinction')



# Distinction# def string_replace(text, ch):
#     replace = ''
#     for i in text:
#         if i == ' ':
#             i = ch
#         replace = replace + i

#     return replace
# text = 'D t C mp'
# ch = 'a'
# print(string_replace(text, ch))


# def binery_search(arr, target):
#     left, right = 0, len(arr)-1
#     while left <= right:
#         mid = (left + right) //2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# arr = [1,2,4,7,9]
# print(binery_search(arr, 1))