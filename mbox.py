fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From ') :continue
	words = line.split()
	email = words[1]
	pieces = email.split('From')
	print pieces[0]
	#print "There were", pieces,"lines in the file with From as the first word"
