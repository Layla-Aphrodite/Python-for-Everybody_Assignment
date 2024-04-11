fname = input("Enter file name: ")
fh = open(fname)
count=0
for line in fh:
    line1=line.rstrip()
    wds=line1.split()
    if len(wds)==0 or wds[0]!='From':
        continue
    print(wds[1].rstrip())
    count=count+1
print("There were",count,"lines in the file with From as the first word")
