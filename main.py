import os
import csv
import time

path = "/mnt/c/developers"

class FileFormat:
    def __init__(self,format,size,path,name):
        self.format = format
        self.amount = 1
        self.size = size
        self.top = {size:{'path':path,'name':name}}
    def plus(self,size,path,name):
        self.amount += 1
        self.size = self.size + size    
        if len(self.top)<10:
            self.top[size]={'path':path,'name':name}
        else:
            mn=min(self.top)
            if size>mn:
                self.top.pop(mn)
                self.top[size]={'path':path,'name':name}
    def out(self):
        # print(self.format,self.amount,self.size)
        return self.format,self.amount,self.size,self.top

        # if len(self.top)>=10:
        #     for i in reversed(sorted(self.top)):
        #         print((i, self.top[i]), end=" ")
        #         (i, self.top[i]), end=" "

       
start = time.time()
d = {}

for root, dirs, files in os.walk(path):
    for name in files:
        x = name.split(".")
        if len(x)>0:
            t = x[len(x)-1].lower()
            if t in d.keys():
                size=os.path.getsize(root+"/"+name)
                p=root+"/"+name 
                ff=d[t] 
                ff.plus(size,p,name)       
                d[t]=ff
            else:
                if os.path.islink(root+"/"+name):
                   pass
                else:
                    size=os.path.getsize(root+"/"+name)
                    p=root+"/"+name 
                    ff=FileFormat(t,size,p,name)
                    d[t]=ff

end = time.time() - start
print("Scan took", end)

header = ['name', 'amount', 'size', 'top']
with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for key,t in d.items():
        writer.writerow(t.out())