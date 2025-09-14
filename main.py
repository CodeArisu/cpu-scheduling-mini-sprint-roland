import algos.FCFS as fcfs
import algos.RoundRobin as rr
from algos.utils.TimeScheduling import run_scheduling

data = {
    'arrv_time': [0, 2, 4, 5, 6],
    'burst_time': [7, 4, 1, 4, 3],
    'quantum': 2
}   

if __name__ == "__main__":
    
    # runs scheduling for the given data and algorithm
    run_scheduling(data, fcfs.FCFS, to_table=True)
    run_scheduling(data, rr.RoundRobin, to_table=True)
