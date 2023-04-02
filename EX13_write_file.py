lines = ['He can take his beak,\n', 'Enough food for a week,\n', 'But I\'m damned if i see how the helican.\n']

with open('pelican.txt', 'a')as infile:
    infile.write('A wonderful bird is the pelican,\n')
    infile.write('His bill holds more than his belican,\n')
    infile.writelines(lines)
# the \n is in place to create a new line after each line of text.
# Otherwise, there would be one lone single string in the txt file.
