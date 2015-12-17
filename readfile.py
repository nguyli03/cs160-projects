file=open('message.txt','r')
line=file.readline().rstrip()
while line!='':
    print(line)
    line=file.readline().rstrip()