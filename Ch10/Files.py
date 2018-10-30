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

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# with open("/home/anushka/Downloads/writefile.txt", "w") as file:
#     for i in color:
#         file.write(i + '\n')



# Write a program to append the times tables to our jabberwocky poem
# in sample.txt. We want the tables from 2 to 12 (similar to the output
# from the For loops part 2 lecture in section 6).
#
# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#  10 times 2 is 20
#  11 times 2 is 22
#  12 times 2 is 24
#  --------------------

# with open("/home/anushka/Downloads/writefile.txt", "a") as file:
#     for times in range(3, 13):
#         for seq in range(1, 13):
#             file.write("#\t{1:>2}\ttimes {0}\tis {2}\n".format(times, seq, seq * times))
#         times += 1
#         file.write("=" * 20 + "\n")

#
# with open("./binaryFiles.txt", "bw") as binFile:
#     for i in range(17):
#         binFile.write(bytes([i]                                                                                                                                                        ))
#
# with open("./binaryFiles.txt", "br") as binFile:
#     for line in binFile:
#         print(line)

# import  shelve
#
# with shelve.open("myshelve.txt") as shelveObj:
#     shelveObj["FirstName"] = "Anil"
#     shelveObj["MiddleName"] = "Kumar"
#     shelveObj["LastName"] = "Narayanan"
#
#     del shelveObj["FirsName"]
#     for key in shelveObj:
#         print(key)
#     # print(shelveObj["FirsName"])
#     # print(shelveObj["MiddleName"])
#     # print(shelveObj["LastName"])

#
# import shelve
#
# shelveObj = shelve.open("myshelve.txt")
# shelveObj["Location"] = "Bangalore"
# shelveObj["State"] = "Karnataka"
#
# for key in sorted(shelveObj.values()):
#     print(key, '-', key)
#
# # shelveObj["State"] = "Kerala"
# #
# # for key in shelveObj:
# #     print(key, '-', shelveObj[key])
#
#
# # while True:
# #     key = input("Enter key: ")
# #     print(shelveObj.get(key))
#
# shelveObj.close()
#
import shelve

FirstName = ["Anil", "Kumar", "Narayanan"]
Location= ["Bangalore"]
Education = ["MIT", "Australia"]

with shelve.open("shelvelists.txt") as file:
    file["FirstName"] = FirstName
    file["Location"] = Location
    file["Education"] = Education

    for listObj in file:
        print(file[listObj])

    file["Location"].append("Karnataka")

    for listObj in file:
        print(file[listObj])
















