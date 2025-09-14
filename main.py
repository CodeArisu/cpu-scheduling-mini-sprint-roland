import algos.FCFS as fcfs
import algos.RoundRobin as rr
from algos.utils.TimeScheduling import run_scheduling, table

data = {
    'arrv_time': [0, 2, 4, 5, 6],
    'burst_time': [7, 4, 1, 4, 3],
    'quantum': 2
}

def main():
    print("Predefined Data:")
    print(table(data.items(), headers=["Parameter", "Values"]))

    if input("Do you want to run FCFS or Round Robin Scheduling? (with Predefined Data) [Y/N]: ").strip().upper() == 'Y':
        choice = input("Enter 'FCFS' or 'RR': ").strip().upper()

        if choice == 'FCFS':
            run_scheduling(data=data, algo=fcfs.FCFS, to_table=True)
        elif choice == 'RR':
            run_scheduling(data=data, algo=rr.RoundRobin, to_table=True)
        else:
            choice = input("Invalid choice. Please enter 'FCFS' or 'RR': ").strip().upper()
            
    else:
        print("Exiting the program.")
        return
    
if __name__ == "__main__":
    main()