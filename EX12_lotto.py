import random
sixnums = 6
numofnums = 0
LottoNums = list(range(1, 51))
selectedNums = list()
welcome = ('###   Welcome to James\'s Lucky Dip Lotto   ###')
print()
print('#'*len(welcome))
print(welcome)
print('#'*len(welcome))
for Nums in LottoNums:
    a = random.choice(LottoNums)
    LottoNums.remove(a)
    selectedNums.append(a)
    numofnums = numofnums+1
    if int(numofnums) == int(sixnums):
        break
Lucky = ('Your lucky numbers are')
length = ((float(len(welcome)-len(Lucky))/2)-1)
print('#'*int(length), Lucky, '#'*int(length))
selectedNumsstr = ''.join(str(selectedNums))
length2 = (((float(len(welcome)-len(selectedNumsstr))/2))-1)
print('#'*int(length2), selectedNumsstr, '#'*int(length2))
print('#'*len(welcome))
print()
