# string = "My name is anil"
# count = 0
# for i in string:
#     print(i, end='')
#     count += 1
#
# print(count)

# string = "google.commmm"
# dic = dict()
# count = 0
# for x in string:
#     for y in string:
#         if x in y:
#             count += 1
#     dic[x] = count
#     count = 0
# print(dic)

# string = 'welcome'
# newString = ''
# if len(string) > 2:
#     newString = string[0:2] + string[-2:]
# else:
#     print(newString)
#
# print(newString)

# string = 'restart'
# ch = string[0]
# newString = string[0]
# for i in string[1:]:
#     if i in ch:
#         newString += '$'
#     else:
#         newString += i
#
# print(newString)

# string1 = 'abc'
# string2 = 'xyz'
#
# newString = string2[:2] + string1[2:] + ' ' + string1[:2] + string2[2:]
# print(newString)

# string = "string"
#
# if len(string) >= 3:
#     if string[-3:] != "ing":
#         string += "ing"
#     else:
#         string += "ly"
#
# print(string)
#
0#
# 0thon function that takes a list of words and returns the length of the longest one'
# 0n"
# 0est"
# 0.split()
# 0
# 0
# 0
0#
# 0:
# 0n i:
# 0
# 0tString.index(i)
# 0g in i:
# 0
# 0tring.index(i)
0#
# 0d)
# 0(splitString[:start]) + " good " + " ".join(splitString[end+1:])
# 0


# string = "Python Debugger Extension Available"
# index = 10
#
# newString = string[:index] + string[index+1:]
#
# print(newString)

string = "Python Debugger Extension Available"
newString = ''
tempCh = string[-1]

newString = str(tempCh) + string[1:-1] + string[0]


print(newString)





















