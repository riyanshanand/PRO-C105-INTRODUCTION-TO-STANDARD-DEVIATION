import csv
import math

with open("data.csv") as f:
    r=csv.reader(f)
    filedata=list(r)
data=filedata[0]    

#lets find the mean
l=len(data)
total=0
for i in data:
    total +=int(i)
mean=total/l
print(mean)    
#lets find (x-u) and square of it
squarelist=[]
for x in data:
    a=int(x)-mean
    r=a*a
    squarelist.append(r)
print(squarelist) 

#lets find the summation of square list
sum=0
for i in squarelist:
    sum += i
print(sum)     
#lets find the N=size of population
N=len(data)-1
print(N) 
result=sum/N
print(result) 
sd=math.sqrt(result)
print(sd)