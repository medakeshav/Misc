read_file = open("input.txt",'r+')
length = int(read_file.readline())
a = range(length)
for line in read_file:
	p = int(line[:line.find(' ')])
	q = int(line[line.find(' ')+1:])
	c = a[p]
	for i in range(length):
		if a[i] == c:
			a[i] = a[q]
print a
read_file.close()