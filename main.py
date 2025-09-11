import algos.FCFS as fcfs
from tabulate import tabulate

data = {
    'arrv_time': [0, 2, 4, 5, 6],
    'burst_time': [7, 4, 1, 4, 3]
}

headers = ["PID", "Arrival Time", "Burst Time", "Start", "Completion Time", "Waiting Time", "Turn Around Time", "Response Time"]

if __name__ == "__main__":
    processes = []
    prev_time = 0
    
    for i in range(len(data['arrv_time'])):
        arrival = data['arrv_time'][i]
        burst = data['burst_time'][i]
        
        start = max(prev_time, arrival)

        comp_time = start + burst
        turn_at = comp_time - arrival
        wait_time = turn_at - burst
        resp_time = start - arrival

        p = fcfs.FCFS(i + 1, arrival, burst, comp_time, start, wait_time, turn_at, resp_time)
        processes.append(p.get())
        
        prev_time = comp_time
        
    n = len(processes)
    avg_tat = sum(p[5] for p in processes) / n
    avg_wt = sum(p[6] for p in processes) / n
    avg_rt = sum(p[7] for p in processes) / n

    processes.append(("Average", "", "", "", "", f"{avg_tat:.2f}", f"{avg_wt:.2f}", f"{avg_rt:.2f}"))

    print("First-Come, First-Served (FCFS) Scheduling Algorithm Results:")
    print(tabulate(processes, headers=headers, tablefmt="fancy_grid", stralign="center", numalign="center"))
