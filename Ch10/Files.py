jabber = open("/home/anushka/Downloads/sample.txt", 'r')

for line in jabber:
    if "jabber" in line.lower():
        print(line)

jabber.close()