import os
#path = "/mnt/a"
path = "/mnt/a"
# one
# {'amount':int,'size':int,'top':{1:['name','path']]}}
# 'type':{} 
# 'size':{'path':'','name':''}

def top(t):
    pass

d = {q} 

for root, dirs, files in os.walk(path):
    for name in files:
        x = name.split(".")
        if len(x)>0:
            t = x[len(x)-1].lower()
            if t in d.keys():
                size=os.path.getsize(root+"/"+name)
                d[t]={'amount':d[t]['amount']+1,'size':d[t]['size']+size}
                # d[t]+=os.path.getsize(root+"/"+name)
            else:
                if os.path.islink(root+"/"+name):
                   pass
                else:
                    size=os.path.getsize(root+"/"+name)
                    d[t]={'amount':1,'size':size} 
for key,t in d.items():
    print(key,t)


        # if name.endswith((".html", ".htm")):
            