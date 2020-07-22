import os

path=os.listdir(os.getcwd())
print(path)
for elem in path:
	f=open(elem,"r")
	l=f.readlines()
	for line in range(len(l)):
		l[line] = l[line].replace(','. '.')

		if "<name>" in l[line]:
        <pose></pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
			l[line]=l[line].replace("2", "small villas")
			l[line]=l[line].replace("1", "large block building")
			l[line]=l[line]+"        <pose></pose>\n        <truncated>0</truncated>\n        <difficult>0</difficult>\n"


	f.close()
	f=open(elem,"w")
	f.writelines(l)
	f.close()

