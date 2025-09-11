import algos.Process as pr
import algos.FCFS as fcfs
from tabulate import tabulate

data = {
    'arrv_time': [0, 2, 4, 5, 6],
    'burst_time': [7, 4, 1, 4, 3]
}

headers = ["PID", "Arrival Time", "Burst Time", "Completion Time", "Waiting Time", "Turn Around Time", "Response Time"]

if __name__ == "__main__":
    processes = []
    prev_time = data['arrv_time'][0]
    
    for i in range(len(data['arrv_time'])):

        prev_time += data['burst_time'][i]
        comp_time = prev_time
        
        p = fcfs.FCFS(i + 1, data['arrv_time'][i], data['burst_time'][i], comp_time)
        processes.append(p.get())
        
    processes.append(("Average", "", "", "", 
                      sum(p[4] for p in processes) / len(processes), 
                      sum(p[5] for p in processes) / len(processes), 
                      sum(p[6] for p in processes) / len(processes)))

    print("First-Come, First-Served (FCFS) Scheduling Algorithm Results:")
    print(tabulate(processes, headers=headers, tablefmt="fancy_grid"))
