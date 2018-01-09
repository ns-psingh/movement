import csv
binary=[]
with open('test5.csv') as csvfile:
    readC=csv.reader(csvfile,delimiter=',')
    totalsum=0
    for avgclc in readC:
        totalsum=totalsum+int(avgclc[0])
    totalavg=totalsum/60000
with open('test5.csv') as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    j=0
    i=0
    sum=0
    avg=0
    for row in readCSV:
        if j<250:
           sum=sum+int(row[0])
           j=j+1
        elif j==250:
            j=0
            avg=sum/250
            if(avg>totalavg):
                print("Yes")
                binary.append("Yes")
            else:
                print("No")
                binary.append("No")
            sum=0
        i=i+1 
csv=open("output5.csv","w")
for bit in binary:
    csv.write(bit+"\n") 