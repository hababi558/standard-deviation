import csv
import math
from os import read

with open('data1.csv',newline='') as f:

    reader=csv.reader(f)
    fileData=list(reader)

data=fileData[0]

def mean(data):
    n = len(data)
    total = 0

    for i in data:

        total += int(i)

    mean = total/n
    return mean

sqr = []

for number in data:
    a = int(number) - mean(data)
    a = a**2
    sqr.append(a)

sum = 0
for j in sqr:
    sum=sum+j     

result = sum/(len(data)-1)
standardDeviation = math.sqrt(result)

print(standardDeviation)

