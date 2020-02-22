#! python3
# pyDictionaryExtractor.py - Used to extract the contents of hard-coded Python
# dictionaries into a CSV formatted file. 

import pyperclip, re
import pyinputplus as pyip

# This script was originally used to extract a dicitonary of capitals from a project
# in Automate the Boring Stuff (https://automatetheboringstuff.com/2e/chapter9/).
# The script has been cleaned up and generalized to read in any hard-coded Python
# dictionary from the user's system's clipboard and save its key-value pairs into
# a CSV file.
#
# Note: this script will work best for hard-coded dictionaries with string to string
# key value pairs. The regex defined below could be modified to find string to
# number, string to list, etc.

# General regex to extract key-value string-to-string pairs from python dictionaries.
dictionaryRegex = re.compile(r'\'(\w+\s*\w*)\':\s+\'(\w+[\s\w+]*)\'')

# Grab the contents of the user's clipboard
text = str(pyperclip.paste())

# Display the copied text to the user.
print('Copied text to search: \n' + text + '\n')

# Ask the user where they'd like to save the file. The user can enter a path to
# save the file to, or they can just enter a filename to save it in the current
# directory.
userInp = pyip.inputFilepath('Where would you like to save the extracted CSV file?\n')

# Write the CSV file to the specified file location.
csvFile = open(userInp, 'w')
for groups in dictionaryRegex.findall(text):
    print(str(groups))
    csvFile.write('%s,%s\n' % (groups[0], groups[1]))

# Display the matches from the regex to the user.
print("Matches found: " + str(len(dictionaryRegex.findall(text))))

# Close the file.
csvFile.close()
