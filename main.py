import algos.FCFS as fcfs
from tabulate import tabulate

data = {
    'arrv_time': [0, 2, 4, 5, 6],
    'burst_time': [7, 4, 1, 4, 3]
}

headers = ["PID", "Arrival Time", "Burst Time", "Start", "Completion Time", "Waiting Time", "Turn Around Time", "Response Time"]

if __name__ == "__main__":
    processes = []
    
    for i in range(len(data['arrv_time'])):
        arrival = data['arrv_time'][i]
        burst = data['burst_time'][i]
        
        obj = fcfs.FCFS(pid=i+1, arrv_time=arrival, burst_time=burst)
        processes.append(obj)

    scheduled = fcfs.FCFS.schedule(processes)
    
    results = [p.get() for p in scheduled]

    avg_tat = sum(p[5] for p in results) / len(results)
    avg_wt = sum(p[6] for p in results) / len(results)
    avg_rt = sum(p[7] for p in results) / len(results)

    results.append(("Average", "", "", "", "", f"{avg_tat:.2f}", f"{avg_wt:.2f}", f"{avg_rt:.2f}"))

    print("First-Come, First-Served (FCFS) Scheduling Algorithm Results:")
    print(tabulate(results, headers=headers, tablefmt="fancy_grid", stralign="center", numalign="center"))
