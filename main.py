import algos.FCFS as fcfs
import algos.RoundRobin as rr
from algos.utils.TimeScheduling import run_scheduling, table

data = {
    'arrv_time': [0, 2, 4, 5, 6],
    'burst_time': [7, 4, 1, 4, 3],
    'quantum': 2
}

def main():
    print("Predefined Dataset (Processes):")
    print(table(data.items(), headers=["Parameter", "Values"]))

    while True:
        choice = input("\nRun Scheduling? (FCFS / RR / Q to quit): ").strip().upper()

        if choice == 'FCFS':
            run_scheduling(data=data, algo=fcfs.FCFS, to_table=True)
        elif choice == 'RR':
            run_scheduling(data=data, algo=rr.RoundRobin, to_table=True)
        elif choice == 'Q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 'FCFS', 'RR', or 'Q'.")
    
if __name__ == "__main__":
    main()