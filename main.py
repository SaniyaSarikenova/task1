#@profile
import statistics
import csv
#import cProfile
import ptest
import time
import line_profiler

y1=time.time()

print('Hello=')

k=0
b=[]
d2=[]
d={}

def upd_dic(d,key,value):
    if key in d:
        d[key].append(value)
    else:
        d[key]=[value]
        d2.append(key)

with open(r'E:\Records.csv') as inf:
    for _ in range(1):
        next(inf)
    for line in inf:
        k+=1
        line=line.strip()
        #print('line ' +line)
        a=line.split(',""')
        #print(a)
        b.append(k)
        #print('a')
        #print(a)
        a.append( a[0].split(','))
        if a[1].count('.')==1:
            upd_dic(d, a[3][0].strip('"'), a[1].strip('"').replace(',', ''))
        else:
            q=[]
            q=a[1].split('"",')
            a.append(q[1])
            upd_dic(d, a[3][0].strip('"'), a[4].strip('"').replace(',', ''))


columns = ['Date', 'Min', 'Max', 'Avg']
with open('E:/out.csv', 'w') as f:
    wr = csv.writer(f,delimiter=';',lineterminator = '\n')
    wr.writerow(columns)
    for i in d2:
        str=[]
        str.append(i)
        str.append(min(d[i], key=lambda i: float(i)))
        str.append(max(d[i], key=lambda i: float(i)))
        x=list(map(float, d[i]))
        str.append(statistics.mean(x))
        wr.writerow(str)

#cProfile.run("ptest.main()")

y2=time.time()
print("%d:%02d:%02d"%((y2-y1), 60*((y2-y1) % 1), 60* (60*((y2-y1) % 1) % 1)))







