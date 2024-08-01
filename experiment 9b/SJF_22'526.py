#Shortest Job First(SJF)
a = int(input("Enter the number of processes -- "))
li = []
p=[]
for i in range(a) :
    li.append(int(input("Enter Brust Time for Process {} -- ".format(i))))
    p.append(i)
for i in range(a-1) :
    for j in range(i,a):
        if(li[i]>li[j]):
            li[i],li[j]=li[j],li[i]
            p[i],p[j]=p[j],p[i]
print("PROCESS\t\tBRUST TIME\tWAITING TIME\tTURNAROUND TIME")
sum1 = 0
wt=[]
tt=[]
for i in range(a):
    wt.append(sum1)
    sum1=sum1+li[i]
    tt.append(sum1)
for i in range(a) :
    print("P",p[i],"\t\t",li[i],"\t\t",wt[i],"\t\t",tt[i],sep="")
avg1=sum(wt)/a
avg2=sum(tt)/a
print("Average Waiting Time --",avg1)
print("Average Turnaround Time --",avg2)
