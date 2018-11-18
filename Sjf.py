bursttime=[5,3,7,10]
processes=["p0","p1","p2","p3"]

for i in range(0,len(bursttime)-1):
  for j in range(0,len(bursttime)-i-1):
     if (bursttime[j]>bursttime[j+1]):
        temp=bursttime[j]
        bursttime[j]=bursttime[j+1]
        bursttime[j+1]=temp
        temp=processes[j]
	processes[j]=processes[j+1]
	processes[j+1]=temp
waitingtime=[]
turnaroundtime=[]
avgwt=0
avgtat=0
waitingtime.insert(0,0)
turnaroundtime.insert(0,bursttime[0])
for i in range(1,len(bursttime)):
   waitingtime.insert(i,waitingtime[i-1]+bursttime[i-1])  
   turnaroundtime.insert(i,waitingtime[i]+bursttime[i]) 
   avgwt+=waitingtime[i]
   avgtat+=turnaroundtime[i]
avgwt=float(avgwt)/len(processes)
avgtat=float(avgtat)/len(processes)
print("\n")
print("processes\t   Burst time\t      waiting time\t    turnaround time\t")
for i in range(0,len(bursttime)):
  print(str(processes[i])+"\t\t\t"+str(bursttime[i])+"\t\t\t"+str(waitingtime[i])+"\t\t\t"+str(turnaroundtime[i]))
  print("\n")
print("Gantt Chart")
print(processes[0]+"....."+processes[1]+"....."+processes[2]+"....."+processes[3])  
print("\n")
print("avearge waiting time is :"+ str(avgwt))
print("avearge turnaround time is :"+ str(avgtat))



