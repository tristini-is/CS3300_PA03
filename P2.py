import numpy as np
import csv

pairArray = []

with open("p2in.txt", "r") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        pairArray.append(line)

xArray = []

for i in range (len(pairArray)):
    xArray.append([1,int(pairArray[i][0])])

yArray = []

for i in range(len(pairArray)):
    yArray.append([int(pairArray[i][1])])

X = np.array(xArray)
Y = np.array(yArray)

XTX = np.dot(np.transpose(X),X)
XTY = np.dot(np.transpose(X),Y)

A = np.round(np.dot(np.linalg.inv(XTX),XTY), decimals=1)

print("y ="+str(A[1][0])+"x+"+str(A[0][0]))

#XTX = np.dot(np.transpose(X),X)


