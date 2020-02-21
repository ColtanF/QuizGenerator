import pyperclip, re

# This was used to extract a dict of capitals from automate the boring stuff
# into a csv file. Actually, this could probably be used for extracting any
# hard-coded python dict into a csv.
# TODO: make this utility file more generalized.
capitalsRegex = re.compile(r'\'(\w+\s*\w*)\':\s+\'(\w+[\s\w+]*)\'')
text = str(pyperclip.paste())
print(text)
capsFile = open('capsFile.txt', 'w')
for groups in capitalsRegex.findall(text):
    print(str(groups))
    capsFile.write('%s,%s\n' % (groups[0], groups[1]))
print("Matches found: " + str(len(capitalsRegex.findall(text))))
# write the matches out to a file
capsFile.close()
