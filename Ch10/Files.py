# jabber = open("/home/anushka/Downloads/sample.txt", 'r')

# for line in jabber:
#     if "jabber" in line.lower():
#         print(line)
#
# jabber.close()


# with open("/home/anushka/Downloads/sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while(line):
#         print(line, end='')
#         line = jabber.readline()

# with open("/home/anushka/Downloads/sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# # print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')

# with open("/home/anushka/Downloads/sample.txt", 'r') as jabber:
#     lines = jabber.read()
#     print(lines)
#     # for line in lines:
#     #     print(line, end='')
#     # lines = jabber.read()

# names = ["Anil", "Kumar", "Narayanan"]
# with open("/home/anushka/Downloads/name.txt", 'w') as files:
#     for name in names:
#         print(name, file=files)

# splitString = list()
# length = 0
# longestWord = ''
# with open("/home/anushka/Downloads/sample.txt", 'r') as file:
#     for line in file:
#         splitString = line.split()
#         for word in splitString:
#             if len(word) > length:
#                 length = len(word)
#                 longestWord = word
#
# print(longestWord, ':', length)

# count = 0
# with open("/home/anushka/Downloads/sample.txt", 'r') as file:
#     for line in file:
#         print(line, end='')
#         count += 1
#
# print(count)

# newDict = {}
# splitString = list()
# with open("/home/anushka/Downloads/sample.txt", 'r') as file:
#     for line in file:
#         splitString = line.split()
#         for word in splitString:
#             if word not in newDict.keys():
#                 newDict[word] = 1
#             else:
#                 temp = newDict[word] + 1
#                 newDict[word] = temp
#
# for i in sorted(newDict):
#     print(i, ':', newDict[i])


# cities = ["Bangalore", "Chennai", "Hyderabad", "Delhi", "Trivandrum"]
#
# with open("/home/anushka/Downloads/writefile.txt", "w") as file:
#     for city in cities:
#         print(city, file=file, end=',', flush=True)

# cities = []
#
# with open("/home/anushka/Downloads/writefile.txt", "r") as file:
#     for line in file:
#         cities.append(line.strip())
#
# print(cities)
#
# for city in cities:
#     print(city)

# cities = ["Bangalore", "Chennai", "Hyderabad", "Delhi", "Trivandrum"]
# newCities = list()
#
# with open("/home/anushka/Downloads/writefile.txt", "w") as file:
#     print(cities, file=file)
#
# with open("/home/anushka/Downloads/writefile.txt", "r") as file:
#     for line in file:
#         newCities = eval(line)
#         print(newCities)
# for city in newCities:
#     print(city)

