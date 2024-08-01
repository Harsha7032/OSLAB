#FIRST COME FIRST SERVE(FCFS)
a = int(input("Enter the number of processes -- "))
li = []
for i in range(a) :
    li.append(int(input("Enter Brust Time for Process {} -- ".format(i))))
print("PROCESS\t\tBRUST TIME\tWAITING TIME\tTURNAROUND TIME")
sum1 = 0
wt=[]
tt=[]
for i in range(a):
    wt.append(sum1)
    sum1=sum1+li[i]
    tt.append(sum1)
for i in range(a) :
    print("P",i,"\t\t",li[i],"\t\t",wt[i],"\t\t",tt[i],sep="")
avg1=sum(wt)/a
avg2=sum(tt)/a
print("Average Waiting Time --",avg1)
print("Average Turnaround Time --",avg2)
