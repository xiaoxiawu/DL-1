import sys
import os

#First arg  = label dir

file = sys.argv[1]
file_name = os.path.splitext(file)[0]

def main():

	with open(file, 'r') as f:
		lines = f.readlines()
	
		for line in lines:
			line = line.strip()
			year = str(int(line[2:6])-1905)
			adjusted_line = str(line + ' ' + year +"\n")
			write(adjusted_line)

def write(new_line):
	with open(file_name + "_adjusted.txt", 'a') as f:
		f.write(new_line)

main()