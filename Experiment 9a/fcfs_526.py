def fcfs_scheduling(burst_times):
    n = len(burst_times)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Calculating waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + burst_times[i-1]
    
    # Calculating turnaround time
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_times[i]
    
    return waiting_time, turnaround_time

def main():
    n = int(input("Enter the number of processes: "))
    burst_times = []
    
    for i in range(n):
        burst_time = int(input(f"Enter burst time for process {i+1}: "))
        burst_times.append(burst_time)
    
    waiting_time, turnaround_time = fcfs_scheduling(burst_times)
    
    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{i+1}\t{burst_times[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

if _name_ == "_main_":
    main()