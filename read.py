with open('my_file.txt', 'w') as f :
	file_data = f.write("test1,test2,test3,test4,test5")
def deal_file(filename):
	listes = []
	with open(filename, 'r') as l:
		for liste in l:
			line_data = liste.split(",")
		for li in line_data :
			x=0
			listes.append(line_data[x])
			x += 1
	return(listes)
x = deal_file("my_file.txt")
print(x)