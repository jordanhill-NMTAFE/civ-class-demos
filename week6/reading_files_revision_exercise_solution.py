# Exercise:
# If you haven't already, download the lyrics of ... 
# BABY SHARK as a txt file, in your work folder.

# Then write a program that reads the file:

# 1. print out only lines containing 'doo'
# 2. count the number of lines containing 'doo'
# 3. count the number of occurrences of the word 'doo;
file = open('baby_shark.txt')
line_count = 0
word_count = 0
for line in file:  
    if 'doo' in line: # filter non-doo lines
        print(line) # 1. prints a doo line
        line_count += 1 # 2. counts doo lines
        for word in line.split(): #splits string into words
            if word == 'doo': # checks if word is doo
                word_count += 1 # 3. count doo words
            
            
print('Doo Line Count:', line_count)
print('Doo Word Count:', word_count)

# snippets
'doo' in line # returns true if substr 'doo' in string line
#count += 1 # is a shorthand for incrementing count by 1
line.split() # splits the words in a line into a list
# a list?? what's a list?
