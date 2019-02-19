import os
fname=input("enter the name of the file:")
infile=open(fname, 'r')
lines=0
words=0
characters=0
for line in infile:
    line = line.strip(os.linesep)
    wordslist=line.split()
    lines=lines+1
    words=words+len(wordslist)
    characters=characters+ len(line)
print(lines)
print(words)
print(characters)