""" Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""

sampleList = ['abc', 'xyz', 'aba', '1221']

for item in sampleList:
    if len(item) >= 2 and item[0] == item[-1]:
        print(sampleList.index(item))