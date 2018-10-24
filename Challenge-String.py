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

string = 'restart'
ch = string[0]
newString = string[0]
for i in string[1:]:
    if i in ch:
        newString += '$'
    else:
        newString += i

print(newString)


































