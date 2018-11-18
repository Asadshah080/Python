# rr schduling algorithm implementation
# python


def findwaitingtime(processes,n,bursttime,waitingtime,quantum):
	rburstt=[0]*n
	for i in range(n):
        	rburstt[i]=bursttime[i]
	time=0
	final=0
	while (1) :
		done=True
        	for k in range(n) :
                	if rburstt[k]>0 :
 	                	done=False
	                	if rburstt[k]>quantum :
                                	time=time+quantum
					rburstt[k]=rburstt[k]-quantum
            			else :
					time=time+rburstt[k]
					waitingtime[k]=time-bursttime[k]
					rburstt[k]=0
		if done==True :break
def findturnaroundtime(processes,n,bt,wt,tat):
	for i in range(n):
        	tat[i]=bt[i]+wt[i]
def findavgtime(processes,n,bt,quantum):
	wt=[0]*n
	tat=[0]*n
	twaitingt=0
	tturnaroundt=0
	findwaitingtime(processes,n,bt,wt,quantum)
	findturnaroundtime(processes,n,bt,wt,tat)
	print("\n")
	print("processes"+"\t\t"+"Burst time"+"\t\t"+"waiting time"+"\t\t"+"turnaround time")
	for i in range(0,n):
        	twaitingt=twaitingt+wt[i]
        	tturnaroundt=tturnaroundt+tat[i]
        	print(str(processes[i])+"\t\t\t"+str(bt[i])+"\t\t\t"+str(wt[i])+"\t\t\t"+str(tat[i]))
        	print("\n")
	
		
	print("avearge waiting time is :"+str (twaitingt/n))
	print("avearge turnaround time is :"+str(tturnaroundt/n))  

if __name__=='__main__': 
	burst_time=[5,3,7,10]
	processes=[1,2,3,4]
	quantum=3	
	n=len(processes)
        findavgtime(processes,n,burst_time,quantum)

