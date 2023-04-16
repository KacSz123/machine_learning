
f1=open('cos.data','r')

line=f1.readlines()
line=list(line)
print(len(line))
line.pop(0)
count = sum(map(lambda x : x!=' ' and x!='\n', line))
print(count)
for i in line:
    print(i,'-', type(i))
print(len(line))





