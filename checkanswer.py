import sys

if len(sys.argv) < 4:
	print("Usage : evalanwser.py answerfile ansCol truthCol")
	sys.exit(1)

i = 0
j = 0
with open(sys.argv[1], 'r') as f:
	for line in f:
		s = line.split(' ')
		if s[int(sys.argv[2])] == s[int(sys.argv[3])].split('-')[0]:
			i += 1
		if not  s[int(sys.argv[2])] in ['39D', '25C', '42C', '32I', '24Q', '4J', '30B', '24O', '21I'] :
			j += 1
		else:
			print  s[int(sys.argv[2])] 
print(i,'/',j)
print(float(i)/j, '%')

