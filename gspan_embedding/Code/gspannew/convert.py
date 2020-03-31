import csv
import os

i=0
length = len([name for name in os.listdir('/home/N1801734D/gspannew/textout/node/')])
print length

while i < length:
	with open('/home/N1801734D/gspannew/textout/node/node' + str(i) + '.txt','r') as in_file:
		#in_file = csv.reader(f)
		stripped = (line.strip() for line in in_file)
		lines = (line.split(" ") for line in stripped if line)
		with open('/home/N1801734D/gspannew/csvout/node' + str(i) + '.csv','w') as out_file:
			writer = csv.writer(out_file)
			writer.writerow(('id' , 'label'))
			writer.writerows(lines)

	with open('/home/N1801734D/gspannew/textout/edge/edge' + str(i) + '.txt','r') as in_file:
		#in_file = csv.reader(f)
		stripped = (line.strip() for line in in_file)
		lines = (line.split(" ") for line in stripped if line)
		with open('/home/N1801734D/gspannew/csvout/edge' + str(i) + '.csv', 'w') as out_file:
			writer = csv.writer(out_file)
			writer.writerow(('source', 'target'))
			writer.writerows(lines)
	
	i = i+1
	
