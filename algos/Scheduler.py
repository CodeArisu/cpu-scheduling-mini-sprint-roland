class SchedulingProcess:
    
    def __init__(self, **kwargs):
        """
        Initialize a Process Simulation instance.
        
        :param pid: Process ID
        :param arrv_time: Arrival Time of the process
        :param burst_time: Burst Time of the process
        :param comp_time: Completion Time of the process
        """
        self.pid = kwargs.get('pid', 0)                # Process ID
        self.arrv_time = kwargs.get('arrv_time', 0)    # Arrival Time
        self.burst_time = kwargs.get('burst_time', 0)  # Burst Time
        self.comp_time = kwargs.get('comp_time', 0)    # Completion Time


    def __repr__(self):
        return f"Process(pid={self.pid}, arrv_time={self.arrv_time}, burst_time={self.burst_time}, comp_time={self.comp_time})"

    def get(self):
        return self.pid, self.arrv_time, self.burst_time, self.comp_time
    
    def compute_completion(self):
        return self.start + self.burst_time
    
    def compute_turnaround(self):
        return self.comp_time - self.arrv_time
    
    def formatted_id(self):
        return f"P{self.pid}"
    
    def to_dict(self):
        return {
            "PID": self.pid,
            "Arrival Time": self.arrv_time,
            "Burst Time": self.burst_time,
            "Completion Time": self.comp_time
        }