from .Scheduler import SchedulingProcess

class RoundRobin(SchedulingProcess):
    def __init__(self, quantum, **kwargs):
        super().__init__(**kwargs)
        self.quantum = quantum
        self.burst_time_rem = self.burst_time
        self.turn_around_time = 0
        self.wait_time = 0
        self.isComplete = False
        self.inQueue = False

    def __repr__(self):
        return (f"RoundRobin(pid={self.pid}, arrv_time={self.arrv_time}, burst_time={self.burst_time}, "
                f"burst_time_rem={self.burst_time_rem}, quantum={self.quantum}, comp_time={self.comp_time}, "
                f"wait={self.wait_time}, tat={self.turn_around_time}, isComplete={self.isComplete})")
        
    @staticmethod
    def schedule(processes):
        """
        Perform Round Robin scheduling on a list of RoundRobin processes.
        """
        from collections import deque

        processes.sort(key=lambda p: p.arrv_time)
        queue = deque()
        time = 0
        completed = 0
        n = len(processes)

        while completed < n:
            # Add all processes that have arrived by current time to the queue
            for proc in processes:
                if proc.arrv_time <= time and not proc.inQueue and not proc.isComplete:
                    queue.append(proc)
                    proc.inQueue = True

            if queue:
                current = queue.popleft()
                exec_time = min(current.burst_time_rem, current.quantum)
                time += exec_time
                current.burst_time_rem -= exec_time

                # If process is completed
                if current.burst_time_rem == 0:
                    current.comp_time = time
                    current.turn_around_time = current.compute_turnaround()
                    current.wait_time = current.turn_around_time - current.burst_time
                    current.isComplete = True
                    completed += 1
                else:
                    # Re-add the process to the end of the queue
                    queue.append(current)
            else:
                # If no process is in the queue, jump to the next arrival time
                next_arrival = min((p.arrv_time for p in processes if not p.isComplete), default=time)
                time = max(time, next_arrival)

        return processes
    
    def get(self):
        return (self.formatted_id(), self.arrv_time, self.burst_time, self.comp_time,
                self.quantum, self.turn_around_time, self.wait_time, self.wait_time)   
    
    def to_dict(self):
        parent = super().to_dict()
        child = {
            "Quantum": self.quantum,
            "Waiting Time": self.wait_time,
            "Turn Around Time": self.turn_around_time,
            "Response Time": self.wait_time
        }
        return {**parent, **child}