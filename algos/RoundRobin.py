from .Scheduler import SchedulingProcess
from collections import deque

class RoundRobin(SchedulingProcess):
    def __init__(self, quantum, **kwargs):
        super().__init__(**kwargs)
        self.quantum = quantum
        self.burst_time_rem = self.burst_time
        self.turn_around_time = 0
        self.wait_time = 0
        self.response_time = None  # track first execution
        self.isComplete = False
        self.inQueue = False

    def __repr__(self):
        return (f"RoundRobin(pid={self.pid}, arrv_time={self.arrv_time}, burst_time={self.burst_time}, "
                f"burst_time_rem={self.burst_time_rem}, quantum={self.quantum}, comp_time={self.comp_time}, "
                f"wait={self.wait_time}, tat={self.turn_around_time}, resp={self.response_time}, "
                f"isComplete={self.isComplete})")

    def get(self):
        return (self.pid, self.arrv_time, self.burst_time,
                self.comp_time, self.quantum,
                self.turn_around_time, self.wait_time, self.response_time)
        
    def to_dict(self):
        parent = super().to_dict()
        child = {
            "Quantum": self.quantum,
            "Turn Around Time": self.turn_around_time,
            "Waiting Time": self.wait_time,
            "Response Time": self.response_time
        }
        return {**parent, **child}
    
    def get_quantum(self):
        return self.quantum
    
    @staticmethod
    def print_gantt_chart(timeline):
        """
        Print a simple timeline for RR, showing each slice executed.
        """
        formatted = [f"({pid}, {start}–{end})" for pid, start, end in timeline]
        print("Timeline:", " ".join(formatted))

    @staticmethod
    def schedule(processes):
        """
        Perform Round Robin scheduling.
        :param processes: list[RoundRobin]
        :return: list[RoundRobin] scheduled
        """
        time = 0
        ready_queue = deque()
        scheduled = []

        # Sort by arrival
        processes.sort(key=lambda p: p.arrv_time)
        n = len(processes)
        remaining = n
        i = 0  # index for arrivals

        # push first arrival
        if processes:
            ready_queue.append(processes[0])
            processes[0].inQueue = True
            i = 1

        while remaining > 0:
            if not ready_queue:
                # no process in queue, jump to next arrival
                time = processes[i].arrv_time
                ready_queue.append(processes[i])
                processes[i].inQueue = True
                i += 1

            proc = ready_queue.popleft()

            if proc.response_time is None:
                proc.response_time = time - proc.arrv_time

            # execute process
            exec_time = min(proc.get_quantum(), proc.burst_time_rem)
            time += exec_time
            proc.burst_time_rem -= exec_time

            while i < n and processes[i].arrv_time <= time:
                if not processes[i].inQueue and not processes[i].isComplete:
                    ready_queue.append(processes[i])
                    processes[i].inQueue = True
                i += 1

            # if process still has burst left then requeue it
            if proc.burst_time_rem > 0:
                ready_queue.append(proc)
            else:
                proc.isComplete = True
                proc.comp_time = time
                proc.turn_around_time = proc.comp_time - proc.arrv_time
                proc.wait_time = proc.turn_around_time - proc.burst_time
                remaining -= 1
                scheduled.append(proc)

        print()
        RoundRobin.print_gantt_chart([(p.formatted_id(), p.comp_time - p.burst_time, p.comp_time) for p in scheduled])
        
        return scheduled