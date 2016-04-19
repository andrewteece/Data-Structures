#Use words.txt as the file name
#Write a program that prompts for a file name, then opens that file
#and reads through the file, and print the contents of the file in upper
#case.

fname = raw_input("Enter a file name: ")
fh = open(fname)
for i in fh:
	i = i.rstrip(),upper()
	print i
	