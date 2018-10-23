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

list1 = ['abc', 'xyz', 'aba', '1221']
list2 = ['abc', 'zy', 'ab', '221']

for item in list1:
    if item in list2:
        print(item)
