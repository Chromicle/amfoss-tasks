import webbrowser as wb
f = open('input.txt')  
lines = f.readlines() 
list = []
for line in lines:
	list+= line.split()
f.close()
print list

search=""

for i in range(0,len(list)):
	search+=list[i]
try:
	wb.get(/home/ajay/.mozilla/firefox/8k4jqapb.default/storage/default).open(list)
