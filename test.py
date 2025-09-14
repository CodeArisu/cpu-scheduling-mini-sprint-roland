import algos.FCFS as fcfs
import algos.RoundRobin as rr
from algos.utils.TimeScheduling import iterate_data, set_processes, header_formatter, run_scheduling

data = {
    'arrv_time': [0, 2, 4, 5, 6],
    'burst_time': [7, 4, 1, 4, 3],
    'quantum': 2
}

run_scheduling(data, rr.RoundRobin, to_table=True)