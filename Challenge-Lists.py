""" Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""

# sampleList = ['abc', 'xyz', 'aba', '1221']
#
# for item in sampleList:
#     if len(item) >= 2 and item[0] == item[-1]:
#         print(sampleList.index(item))

# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


# def last(n): return n[1]
#
#
# sampleList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#
# print(sampleList[1][1])
# print(sorted(sampleList, key=last))

# sampleList = ['a', 'b', 'c', 'b']
#
# noDuplicate = list()
#
# for i in sampleList:
#     if i not in noDuplicate:
#         noDuplicate.append(i)
#
# print(noDuplicate)


# sampleList = ['a', 'b', 'c', 'b']
# secondList = list(sampleList)
# secondList[0] = 'd'
#
# print(sampleList)
# print(secondList)
#
# string = 'The quick brown fox jumps over the lazy dog'
#
# length = int(input("Enter length: "))
#
# words = string.split(' ')
# for word in words:
#     if len(word) > length:
#         print(word)

# list1 = ['abc', 'xyz', 'aba', '1221']
# list2 = ['abcd', 'zy', 'ab', '221']
#
# for item in list1:
#     if item in list2:
#         print(item)

# sampleList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# sampleList.remove(sampleList[0])
# sampleList.remove(sampleList[4])
# # sampleList.remove(sampleList[5])
# print(sampleList)

# num = [1,2,3,4,5,7,8,9,10]
#
# for i in num:
#     if i not in range(0, 100, 2):
#         print(i)

# numList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#
# counter = 1
# for i in range(1,30):
#     # if (i > 0 and i <= 5) or (i >= 25 and i <= 30):
#     if (0 < i <= 5) or (25 <= i <= 30):
#         print(i * i)
#

# numList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#
# for i in numList:
#     for j in numList:
#         print(i * j)


# numList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#
# newList = [1, 3, 2]
# resultList = list()
# print(list(set(numList).difference(set(newList))))
# print(list(set(numList) - (set(newList))))
# for i in numList:
#     if i not in newList:
#         resultList.append(i)
#
# print(resultList)

# numList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#
# index = 0
# for i in numList:
#     print(index, ' ', i)
#     index += 1


# chList = ['a', 'b', 'c', 'd', 'e']
# string = ""
#
#
# for i in chList:
#     string = string + i
#
# print(string)
#
# string = "".join(chList)
# print(string)






















