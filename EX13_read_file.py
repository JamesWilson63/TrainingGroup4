file = open('pelican.txt','r')
data = file.read()
print(data)
# This is displayed as a string.
data_into_list = data.replace('\n',' ').split(",")
print(data_into_list)
print()
print("There are :", len(data_into_list), "Items in this list")
print()
for i in data_into_list:
    print(i)
