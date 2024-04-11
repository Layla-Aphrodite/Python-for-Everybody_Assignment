name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
time=dict()
lst=list()

for line in handle:
    if not line.startswith("From "):
        continue
    wrd=line.split()
    hour=wrd[5].split(":")
    hour=hour[0]
    lst.append(hour)

    
for w in lst:
    time[w]=time.get(w,0)+1

for k,v in sorted(time.items()):
    print(k,v)
