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

names = ["Anil", "Kumar", "Narayanan"]
with open("/home/anushka/Downloads/name.txt", 'w') as files:
    for name in names:
        print(name, file=files)