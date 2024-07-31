def sjf_scheduling(burst_times):
    n = len(burst_times)
    processes = list(range(n))
    
    # Sorting processes based on burst time
    processes.sort(key=lambda x: burst_times[x])
    
    waiting_time = [0] * n
    turnaround_time = [0] * n
    elapsed_time = 0
    
    # Calculating waiting time and turnaround time
    for i in range(n):
        process = processes[i]
        waiting_time[process] = elapsed_time
        turnaround_time[process] = waiting_time[process] + burst_times[process]
        elapsed_time += burst_times[process]
    
    return waiting_time, turnaround_time

def main():
    n = int(input("Enter the number of processes: "))
    burst_times = []
    
    for i in range(n):
        burst_time = int(input(f"Enter burst time for process {i+1}: "))
        burst_times.append(burst_time)
    
    waiting_time, turnaround_time = sjf_scheduling(burst_times)
    
    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{i+1}\t{burst_times[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

if _name_ == "_main_":
    main()