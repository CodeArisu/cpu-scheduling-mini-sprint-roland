from .Scheduler import SchedulingProcess

class FCFS(SchedulingProcess):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wait_time = 0
        self.turn_around_time = 0
        self.response_time = 0
        self.start = 0

    def __repr__(self):
        return (f"FCFS(pid={self.pid}, arrv_time={self.arrv_time}, burst_time={self.burst_time}, "
                f"start={self.start}, comp_time={self.comp_time}, wait={self.wait_time}, "
                f"tat={self.turn_around_time}, resp={self.response_time})")

    def compute_start(self, prev_time):
        return max(prev_time, self.arrv_time)

    def compute_wait(self):
        return self.turn_around_time - self.burst_time
    
    def compute_completion(self):
        return self.start + self.burst_time

    def compute_response(self):
        return self.start - self.arrv_time

    def first_come_first_serve(self, prev_time):
        """
        Compute all metrics for this process given the previous completion time.
        """
        self.start = self.compute_start(prev_time)
        self.comp_time = self.compute_completion()
        self.turn_around_time = self.compute_turnaround()
        self.wait_time = self.compute_wait()
        self.response_time = self.compute_response()
        return self
    
    def to_dict(self):
        parent = super().to_dict()
        child = {
            "Start": self.start,
            "Waiting Time": self.wait_time,
            "Turn Around Time": self.turn_around_time,
            "Response Time": self.response_time
        }
        return {**parent, **child}

    @staticmethod
    def print_gantt_chart(processes):
        """
        Print a simple Gantt timeline as [(P1, 0–7), (P2, 7–11), ...]
        """
        timeline = []
        for p in processes:
            timeline.append(f"(P{p.pid}, {p.start}–{p.comp_time})")

        print("Timeline:", " ".join(timeline))

    @staticmethod
    def schedule(processes):
        """
        Perform FCFS scheduling on a list of FCFS processes.
        """
        processes.sort(key=lambda p: p.arrv_time)

        prev_time = 0
        scheduled = []
        for proc in processes:
            proc.first_come_first_serve(prev_time)
            prev_time = proc.comp_time
            scheduled.append(proc)
        
        print()
        FCFS.print_gantt_chart(scheduled)

        return scheduled

    def get(self):
        return (self.formatted_id(), self.arrv_time, self.burst_time,
                self.comp_time, self.start, self.wait_time,
                self.turn_around_time, self.response_time)
