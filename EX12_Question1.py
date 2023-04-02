# What is wrong with this?
#       This command will add each letter as a seperate item in the list.

cheese = ['Chedder', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
print(cheese)

del cheese[3:]

# How should 'Oke' be added to the end of the cheese list?
#       We can use [] Brackets to show that each item in comas is a single element
#       Or we can use an alternate function (.append).

cheese.append('Oke')
print(cheese)

# How would you add two new cheeses to the list with a single command?
#       += or .extend

cheese += ['Danish Blue', 'Edam']
print(cheese)
