def header_formatter(obj:object):
    return list(obj.keys())

def calc_avg(processes, index):
    return sum(p[index] for p in processes) / len(processes)

def table(processes, headers):
    from tabulate import tabulate
    return tabulate(processes, headers=headers, tablefmt="fancy_grid", stralign="center", numalign="center")

def iterate_data(data):
    for index in range(len(data['arrv_time'])):
        arrival = data['arrv_time'][index]
        burst = data['burst_time'][index]
        yield (arrival, burst)

def set_processes(data, scheduling_algo):
    processes = []
    
    if scheduling_algo is None:
        raise ValueError("scheduling_algo must be provided")
    
    if scheduling_algo.__name__ not in ['FCFS', 'RoundRobin']:
        raise ValueError("Unsupported scheduling algorithm. Supported: FCFS, RoundRobin")
    
    if scheduling_algo.__name__ == 'FCFS':
        for arrival, burst in iterate_data(data):
            obj = scheduling_algo(pid=len(processes)+1, arrv_time=arrival, burst_time=burst)
            processes.append(obj)
            
    elif scheduling_algo.__name__ == 'RoundRobin':
        if 'quantum' not in data:
            raise ValueError("Quantum time must be provided for RoundRobin scheduling")
        
        quantum = data['quantum']
        for arrival, burst in iterate_data(data):
            obj = scheduling_algo(pid=len(processes)+1, arrv_time=arrival, burst_time=burst, quantum=quantum)
            processes.append(obj)
            
    else:
        raise ValueError("Unsupported scheduling algorithm")
    
    return processes

def schedule_results(processes, scheduling_algo):
    scheduling_algo.schedule(processes)
    results = [p.get() for p in processes]
    
    avg_tat = calc_avg(results, 5)
    avg_wt = calc_avg(results, 6)
    avg_rt = calc_avg(results, 7)
    
    results.append(("Average", "", "", "", "", f"{avg_tat:.2f}", f"{avg_wt:.2f}", f"{avg_rt:.2f}"))
    return results

def run_scheduling(data, algo, to_table=True):
    processes = set_processes(data, algo)
    results = schedule_results(processes, algo)
    if to_table:
        headers = header_formatter(algo().to_dict() if algo.__name__ == 'FCFS' else algo(quantum=data['quantum']).to_dict())
        print("Scheduling Results:")
        print(table(results, headers=headers))
    else:
        for result in results:
            print(result)
    return results